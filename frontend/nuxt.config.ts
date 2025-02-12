// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: ["@nuxt/ui", "nuxt-socket-io"],

  colorMode: {
    preference: 'dark'
  },

  io: {
    // module options
    sockets: [
      {
        name: 'main',
        url: 'http://localhost:5000',
        default: true,
        vuex: {
          mutations: [],
          actions: []
        },
        namespaces: {
          '/index': {
            emitters: ['method1', 'audio'],
            listeners: ['someEvent', 'transcription']
          }
        }
      }
    ]
  },

  compatibilityDate: '2025-01-08'
})