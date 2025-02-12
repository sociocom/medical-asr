<template>
    <div>
    <UContainer>
      <UCard class="mt-10">
        <template #header>
          <div class="flex justify-between">
            <h1>Welcome to Nuxt UI Starter</h1>
          </div>
        </template>
        <UButton icon="i-heroicons-book-open" to="https://ui.nuxt.com" target="_blank">Open Nuxt UI Documentation</UButton>
      </UCard>
    </UContainer>
    <UContainer> 
      <UDivider label="OR" />
    </UContainer>
    <UContainer>
      <UIcon name="i-heroicons-light-bulb" class="w-5 h-5" />
  
   <UAvatarGroup size="sm" :max="2">
      <UAvatar
        src="https://avatars.githubusercontent.com/u/739984?v=4"
        alt="benjamincanac"
      />
      <UAvatar
        src="https://avatars.githubusercontent.com/u/904724?v=4"
        alt="Atinux"
      />
      <UAvatar
        src="https://avatars.githubusercontent.com/u/7547335?v=4"
        alt="smarroufin"
      />
    </UAvatarGroup> 
    <UCheckbox label="Label" :model-value="false" />
  
    </UContainer>
  </div>
    
  </template>
  