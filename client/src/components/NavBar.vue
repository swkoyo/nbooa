<script setup lang="ts">
import router from '@/router';
</script>

<template>
    <nav>
        <div class='flex flex-row w-full dark:bg-slate-900 absolute top-0 p-4'>
            <div @click="router.push('/')" class="inline-flex items-center space-x-2 hover:cursor-pointer">
                <img class='h-10' src="../assets/logo.png" />
                <h1 class='text-xl font-bold'>NBooA</h1>
            </div>
            <div class='flex-1' />
            <button @click="router.push('/players')"
                class='bg-indigo-500 rounded-lg p-2 text-md font-medium hover:bg-opacity-40'>Players</button>
        </div>
    </nav>
</template>