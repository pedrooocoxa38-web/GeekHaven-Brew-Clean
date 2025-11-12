/**
 * API Client for GeekHaven Brew Backend
 * Handles all HTTP communication with FastAPI backend
 */

// Configuração da URL da API - produção vs desenvolvimento
const getApiUrl = () => {
  // Primeira prioridade: variável de ambiente VITE_API_URL
  if (import.meta.env.VITE_API_URL) {
    return import.meta.env.VITE_API_URL;
  }
  
  // Segunda prioridade: detectar ambiente automaticamente
  const isDev = import.meta.env.DEV;
  const isProd = import.meta.env.PROD;
  
  if (isDev) {
    return 'http://localhost:8000/api';
  }
  
  if (isProd) {
    // URL de produção do EasyPanel
    return 'https://geekhaven-brew-1-cafeteria-back-1.a9negi.easypanel.host/api';
  }
  
  // Fallback
  return 'http://localhost:8000/api';
};

const API_URL = getApiUrl();

// Debug log para verificar a URL que está sendo usada
console.log('🔗 API URL configurada:', API_URL);
console.log('🔧 Ambiente:', import.meta.env.MODE);
console.log('🚀 Produção:', import.meta.env.PROD);
console.log('🛠️ Desenvolvimento:', import.meta.env.DEV);

// Types
export interface User {
  id: number;
  name: string;
  email: string;
  role: string;
}

export interface Product {
  id: number;
  name: string;
  description: string;
  price: number;
  category: string;
  image?: string;
  stock: number;
}

export interface CartItem {
  id: number;
  product_id: number;
  quantity: number;
  product: Product;
}

export interface Cart {
  items: CartItem[];
  total: number;
}

export interface Reservation {
  id: number;
  user_id: number;
  date: string;
  time: string;
  people_count: number;
  status: string;
  created_at: string;
}

export interface Order {
  id: number;
  user_id: number;
  total: number;
  status: string;
  created_at: string;
  items: OrderItem[];
}

export interface OrderItem {
  id: number;
  product_id: number;
  quantity: number;
  price: number;
  product: Product;
}

export interface LoginResponse {
  access_token: string;
  token_type: string;
}

// Helper function to get auth headers
const getAuthHeaders = () => {
  const token = localStorage.getItem('access_token');
  return {
    'Content-Type': 'application/json',
    ...(token && { Authorization: `Bearer ${token}` }),
  };
};

// API Error handler
class APIError extends Error {
  constructor(public status: number, message: string) {
    super(message);
    this.name = 'APIError';
  }
}

// Generic fetch wrapper
const apiRequest = async <T>(
  endpoint: string, 
  options: RequestInit = {}
): Promise<T> => {
  const url = `${API_URL}${endpoint}`;
  
  console.log('🚀 Fazendo requisição para:', url);
  console.log('🔧 Opções:', options);
  
  const config: RequestInit = {
    headers: getAuthHeaders(),
    ...options,
  };

  try {
    const response = await fetch(url, config);
    console.log('📡 Resposta recebida:', {
      status: response.status,
      statusText: response.statusText,
      headers: Object.fromEntries(response.headers.entries()),
      url: response.url
    });
    
    if (!response.ok) {
      const errorData = await response.json().catch(() => null);
      console.error('❌ Erro na API:', {
        status: response.status,
        statusText: response.statusText,
        errorData,
        url
      });
      throw new APIError(
        response.status, 
        errorData?.detail || errorData?.message || `HTTP ${response.status}: ${response.statusText}`
      );
    }

    // Handle 204 No Content responses
    if (response.status === 204) {
      return {} as T;
    }

    const data = await response.json();
    console.log('✅ Dados recebidos:', data);
    return data;
  } catch (error) {
    if (error instanceof APIError) {
      throw error;
    }
    
    // Network or other errors
    console.error('🔥 Falha na requisição da API:', {
      error,
      url,
      message: error instanceof Error ? error.message : 'Erro desconhecido'
    });
    
    // Mais informações sobre o tipo de erro
    if (error instanceof TypeError && error.message.includes('fetch')) {
      throw new APIError(0, `Erro de conectividade. Verifique se o backend está rodando em: ${API_URL.replace('/api', '')}`);
    }
    
    throw new APIError(0, 'Erro de conexão. Verifique sua internet e tente novamente.');
  }
};

// Auth API
export const authAPI = {
  async login(email: string, password: string): Promise<LoginResponse> {
    return apiRequest<LoginResponse>('/auth/login', {
      method: 'POST',
      body: JSON.stringify({ email, password }),
    }).then(data => {
      // Store token in localStorage
      localStorage.setItem('access_token', data.access_token);
      return data;
    });
  },

  async register(name: string, email: string, password: string): Promise<User> {
    return apiRequest<User>('/auth/register', {
      method: 'POST',
      body: JSON.stringify({ name, email, password }),
    });
  },

  async getCurrentUser(): Promise<User> {
    return apiRequest<User>('/auth/profile');
  },

  logout(): void {
    localStorage.removeItem('access_token');
  },

  isAuthenticated(): boolean {
    return !!localStorage.getItem('access_token');
  },
};

// Products API
export const productsAPI = {
  async getAll(): Promise<Product[]> {
    console.log('🔗 Chamando API de produtos:', `${API_URL}/products`);
    const result = await apiRequest<Product[]>('/products');
    console.log('📦 Produtos retornados da API:', result);
    return result;
  },

  async getById(id: number): Promise<Product> {
    return apiRequest<Product>(`/products/${id}`);
  },

  async create(product: Partial<Product>): Promise<Product> {
    return apiRequest<Product>('/products', {
      method: 'POST',
      body: JSON.stringify(product),
    });
  },

  async update(id: number, product: Partial<Product>): Promise<Product> {
    return apiRequest<Product>(`/products/${id}`, {
      method: 'PUT',
      body: JSON.stringify(product),
    });
  },

  async delete(id: number): Promise<void> {
    return apiRequest<void>(`/products/${id}`, {
      method: 'DELETE',
    });
  },
};

// Cart API
export const cartAPI = {
  async get(userId: number): Promise<Cart> {
    return apiRequest<Cart>(`/cart/${userId}`);
  },

  async addItem(productId: number, quantity: number = 1): Promise<{ message: string; detail: string }> {
    return apiRequest<{ message: string; detail: string }>('/cart/add', {
      method: 'POST',
      body: JSON.stringify({ product_id: productId, quantity }),
    });
  },

  async updateItem(itemId: number, quantity: number): Promise<{ message: string; detail: string }> {
    return apiRequest<{ message: string; detail: string }>(`/cart/update/${itemId}`, {
      method: 'PUT',
      body: JSON.stringify({ quantity }),
    });
  },

  async removeItem(itemId: number): Promise<{ message: string; detail: string }> {
    return apiRequest<{ message: string; detail: string }>(`/cart/remove/${itemId}`, {
      method: 'DELETE',
    });
  },

  async checkout(): Promise<{ message: string; detail: string }> {
    return apiRequest<{ message: string; detail: string }>('/cart/checkout', {
      method: 'POST',
    });
  },
};

// Reservations API
export const reservationsAPI = {
  async create(reservation: {
    date: string;
    time: string;
    people_count: number;
  }): Promise<Reservation> {
    return apiRequest<Reservation>('/reservations', {
      method: 'POST',
      body: JSON.stringify(reservation),
    });
  },

  async update(id: number, reservation: {
    date?: string;
    time?: string;
    people_count?: number;
    status?: string;
  }): Promise<Reservation> {
    return apiRequest<Reservation>(`/reservations/${id}`, {
      method: 'PUT',
      body: JSON.stringify(reservation),
    });
  },

  async cancel(id: number): Promise<{ message: string; detail: string }> {
    return apiRequest<{ message: string; detail: string }>(`/reservations/${id}`, {
      method: 'DELETE',
    });
  },

  async getUserReservations(userId: number): Promise<Reservation[]> {
    return apiRequest<Reservation[]>(`/reservations/user/${userId}`);
  },

  async getAll(): Promise<Reservation[]> {
    return apiRequest<Reservation[]>('/reservations');
  },

  async updateStatus(id: number, status: string): Promise<Reservation> {
    return apiRequest<Reservation>(`/reservations/${id}/status`, {
      method: 'PUT',
      body: JSON.stringify({ status }),
    });
  },
};

// Orders API
export const ordersAPI = {
  async getUserOrders(userId: number): Promise<Order[]> {
    return apiRequest<Order[]>(`/orders/user/${userId}`);
  },

  async getAll(): Promise<Order[]> {
    return apiRequest<Order[]>('/orders');
  },

  async updateStatus(id: number, status: string): Promise<Order> {
    return apiRequest<Order>(`/orders/${id}/status`, {
      method: 'PUT',
      body: JSON.stringify({ status }),
    });
  },
};

// Test API connection
export const testAPI = {
  async ping(): Promise<{ message: string }> {
    return apiRequest<{ message: string }>('/test');
  },
};

// Default export with all APIs
const api = {
  auth: authAPI,
  products: productsAPI,
  cart: cartAPI,
  reservations: reservationsAPI,
  orders: ordersAPI,
  test: testAPI,
};

export default api;