<script setup lang="ts">
import router from '@/router';
import MainContainer from '../layouts/MainContainer.vue'
</script>

<template>
  <MainContainer>
    <div class='flex flex-row w-full h-fit my-auto space-x-10'>
      <div class="basis-1/2 justify-center my-auto space-y-10 pr-10">
        <div class='space-y-3'>
          <h1 class='text-6xl font-bold'>Find useless stats!</h1>
          <h3 class='text-lg'>Ever wonder how many points LeBron scored on his birthday? How about on Valentine's? NBooA
            allows you to view player stats that you'll never need.</h3>
        </div>
        <button @click="router.push('/players')" class='bg-indigo-500 rounded-full p-2 text-sm text-white'>
          View Players
        </button>
      </div>
      <div class="basis-1/2 p-4">
        <img
          src="https://advancelocal-adapter-image-uploads.s3.amazonaws.com/image.cleveland.com/home/cleve-media/width2048/img/datacentral/photo/lebron-james-birthday-09192d395471f026.jpg" />
      </div>
    </div>
  </MainContainer>
</template>
