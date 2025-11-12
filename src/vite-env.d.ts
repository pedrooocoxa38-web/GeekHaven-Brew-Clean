/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_API_URL: string
  readonly VITE_APP_TITLE: string
  readonly VITE_APP_DESCRIPTION: string
  readonly VITE_DEBUG_MODE: string
  readonly MODE: string
  readonly DEV: boolean
  readonly PROD: boolean
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}
