<script setup lang="ts">
import type { Player } from '../types'
import { formatDate } from '../utils/date'
import router from '@/router';
defineProps<{
    player: Player
}>()
</script>

<template>
    <div @click="router.push(`/players/${player._id}`)" class='shadow-md bg-gray-50 p-4 rounded-lg'>
        <img :src="player.image_url" />
        <p>{{ player.first_name }} {{ player.last_name }}</p>
        <p>{{ formatDate(player.birthday) }}</p>
        <p>{{ player.start_year }} ~ {{ player.end_year || 'current' }}</p>
    </div>
</template>
