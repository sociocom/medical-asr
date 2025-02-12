<template>
    <div :class="layoutClass">
      
      <div :class="sectionLayoutClass">
        <h4 class="text-5xl bg-teal-500 text-black p-2 w-full text-center">原文</h4>
        <div class="mt-4 p-8">
          <p class="text-teal-500 text-6xl">
            <span v-html="currentTranscription"></span>
          </p>
        </div>
      </div>

      <div v-if="displayMode !== 'vertical'" class="border-l-4 border-teal-500"></div>
      <br v-if="displayMode === 'vertical'">
  
      <div :class="sectionLayoutClass">
        <h4 class="text-5xl bg-teal-500 text-black p-2 w-full text-center">簡略化</h4>
        <div class="mt-4 p-8">
          <p class="text-teal-500 text-6xl">
            <span v-html="currentSimplification"></span>
          </p>
        </div>
      </div>
      
    </div>
  </template>
  
  <script setup>  
  const props = defineProps({
    displayMode: String,
    currentTranscription: String,
    currentSimplification: String
  })
  
  const getClass = (horizontalClass, verticalClass) => {
    return props.displayMode === 'horizontal' ? horizontalClass : verticalClass
  }
  
  const layoutClass = computed(() => getClass('h-[80vh] w-full flex border-teal-500 border-4 rounded-2xl', 'space-y-4'))
  const sectionLayoutClass = computed(() => getClass('w-1/2 flex flex-col items-start', 'h-[40vh] w-full flex flex-col items-start border-teal-500 border-4 rounded-2xl'))
  </script>