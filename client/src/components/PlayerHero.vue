<script setup lang="ts">
import type { Player } from '@/types';
import { formatDate } from '@/utils/date'
import { defineProps } from 'vue';
defineProps<{
    player: Player
}>()
</script>

<template>
    <div class='flex flex-row w-full h-fit bg-slate-500'>
        <div class='basis-1/3'>
            <img :src="player.image_url" />
        </div>
        <div class='basis-2/3'>
            <h1>{{ player.first_name }} {{ player.last_name }}</h1>
            <p>{{ player.first_name }} {{ player.last_name }}</p>
            <p>{{ formatDate(player.birthday) }}</p>
            <p>{{ player.start_year }} ~ {{ player.end_year || 'current' }}</p>
        </div>
    </div>
</template>