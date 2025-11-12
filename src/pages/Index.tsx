import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import HeroCarousel from "@/components/HeroCarousel";
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { Coffee, Gamepad2, Users, Clock } from "lucide-react";
import { useNavigate } from "react-router-dom";

const Index = () => {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen bg-background">
      <Navbar />
      
      <main className="pt-16">
        {/* Hero Section */}
        <section className="container mx-auto px-4 py-8">
          <HeroCarousel />
        </section>

        {/* Features */}
        <section className="container mx-auto px-4 py-16">
          <div className="grid md:grid-cols-4 gap-6">
            {[
              { icon: Coffee, title: "Café Premium", desc: "Bebidas de alta qualidade" },
              { icon: Gamepad2, title: "Setup Gamer", desc: "PCs e consoles top de linha" },
              { icon: Users, title: "Eventos", desc: "Espaço para torneios" },
              { icon: Clock, title: "Aberto 24/7", desc: "Sempre disponível para você" }
            ].map((feature, index) => (
              <Card key={index} className="p-6 text-center space-y-3 hover-lift">
                <div className="w-12 h-12 bg-primary/10 rounded-full flex items-center justify-center mx-auto">
                  <feature.icon className="h-6 w-6 text-primary" />
                </div>
                <h3 className="font-semibold text-lg">{feature.title}</h3>
                <p className="text-sm text-muted-foreground">{feature.desc}</p>
              </Card>
            ))}
          </div>
        </section>

        {/* CTA Section */}
        <section className="container mx-auto px-4 py-16">
          <Card className="relative overflow-hidden">
            <div className="absolute inset-0 bg-gradient-to-r from-primary to-secondary opacity-10" />
            <div className="relative p-12 text-center space-y-6">
              <h2 className="text-3xl md:text-5xl font-bold">
                Pronto para a Experiência?
              </h2>
              <p className="text-xl text-muted-foreground max-w-2xl mx-auto">
                Venha conhecer a melhor cafeteria geek da cidade. Café premium, jogos e diversão garantida!
              </p>
              <div className="flex flex-col sm:flex-row gap-4 justify-center">
                <Button 
                  size="lg" 
                  className="shadow-glow"
                  onClick={() => navigate('/products')}
                >
                  Fazer Pedido
                </Button>
                <Button 
                  size="lg" 
                  variant="secondary"
                  onClick={() => navigate('/reservations')}
                >
                  Reservar Espaço
                </Button>
              </div>
            </div>
          </Card>
        </section>
      </main>

      <Footer />
    </div>
  );
};

export default Index;
