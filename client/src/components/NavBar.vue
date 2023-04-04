<script setup lang="ts">
import router from '@/router';
</script>

<template>
    <nav>
        <div class='flex flex-row w-full bg-blue-400 absolute top-0 p-4'>
            <div>NBooA</div>
            <div class='flex-1' />
            <button @click="router.push('/')" class='bg-blue-400 rounded-sm p-2'>Home</button>
            <button @click="router.push('/players')" class='bg-blue-400 rounded-sm p-2'>Players</button>
        </div>
    </nav>
</template>