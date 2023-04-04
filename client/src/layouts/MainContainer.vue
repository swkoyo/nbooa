<script setup lang="ts">
import NavBar from '../components/NavBar.vue'
</script>

<template>
    <main class='bg-gray-300'>
        <NavBar />
        <div class='flex w-full min-h-screen h-full max-w-7xl mx-auto p-10'>
            <slot></slot>
        </div>
    </main>
</template>