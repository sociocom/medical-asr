<template>
  <UModal :model-value="props.isModalOpen" @update:model-value="updateModalVisible">
    <div class="h-[50vh] bg-black p-8 rounded-2xl space-y-4 overflow-y-scroll">
      <h2 class="text-5xl text-teal-500">トランスクリプト履歴</h2>  
      <div class="space-y-4">
        <div v-for="transcription in transcriptions" :key="transcription.date" class="w-full flex flex-col items-start border-teal-500 border-4 rounded-2xl">
          <h4 class="text-xl bg-teal-500 text-black p-2 w-full text-center rounded">原文 {{ transcription.date.toUTCString() }}</h4>
          <div class="mt-2 p-2">
            <p class="text-teal-500 text-2xl" v-html="transcription.text"></p>
          </div>
        </div>
      </div>
    </div>
  </UModal>
  </template>
  
  <script setup>
  
  const props = defineProps({
    isModalOpen: Boolean,
    transcriptions: Array
  })
  
  const emit = defineEmits(['update:isModalOpen'])
  const updateModalVisible = (value) => {
    emit('update:isModalOpen', value)
  }

  </script>