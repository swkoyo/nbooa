<script setup lang="ts">
import type { Player } from '../types'
import { formatDate } from '../utils/date'
import router from '@/router';
defineProps<{
    player: Player
}>()
</script>

<template>
    <div class='flex flex-col shadow-lg border border-slate-700 rounded-md'>
        <img class='bg-black bg-opacity-60 rounded-t-md' :src="player.image_url" />
        <div class='flex flex-col p-6 space-y-8'>
            <div class='flex w-full'>
                <div class='flex flex-col basis-1/2 font-light'>
                    <p>Name</p>
                    <p>Birthday</p>
                    <p>Years Active</p>
                </div>
                <div class='flex flex-col basis-1/2 font-bold'>
                    <p class='truncate'>{{ player.first_name }} {{ player.last_name }}</p>
                    <p>{{ formatDate(player.birthday) }}</p>
                    <p>{{ player.start_year }} ~ {{ player.end_year || 'current' }}</p>
                </div>
            </div>
            <button @click="router.push(`/players/${player._id}`)"
                class='rounded-full w-fit px-3 py-2 text-sm font-bold mx-auto bg-indigo-500 hover:cursor-pointer hover:bg-opacity-50'>View
                Stats</button>
        </div>
    </div>
</template>
