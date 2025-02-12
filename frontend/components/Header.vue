<template>
    <div class="h-[10vh] w-full flex items-center justify-between space-x-4">
      
      <UTooltip text="バックエンドテスト">
        <UButton @click="requestDummyData" color="teal" class="text-black px-4 py-3 rounded">
          <UIcon name="i-material-symbols-play-arrow" class="text-4xl"/>
        </UButton>
      </UTooltip>
      
      <div class="flex-grow"></div>
      <h3 class="text-7xl flex-grow text-teal-500">医療音声認識</h3>
      
      <UTooltip text="トランスクリプトの表示">
        <UButton @click="toggleModal" color="teal" class="text-black px-4 py-3 rounded">
          <UIcon name="i-stash-version-solid" class="text-4xl"/>
        </UButton>
      </UTooltip>
      
      <UTooltip text="表示モードの変更">
        <UButton @click="toggleDisplay" color="teal" class="text-black px-4 py-3 rounded">
          <UIcon name="i-humbleicons-exchange-horizontal" class="text-4xl"/>
        </UButton>
      </UTooltip>

    </div>
  </template>
  
  <script setup>
  const props = defineProps({
    requestDummyData: Function,
    toggleModal: Function,
    toggleDisplay: Function,
  })
  </script>