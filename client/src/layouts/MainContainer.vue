<script setup lang="ts">
import NavBar from '../components/NavBar.vue'
</script>

<template>
    <main class='bg-slate-800 text-white'>
        <NavBar />
        <div class='flex flex-col w-full min-h-screen h-full max-w-7xl mx-auto px-10 pt-24 pb-8'>
            <slot></slot>
        </div>
    </main>
</template>