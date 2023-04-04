<script setup lang="ts">
import type { Player } from '@/types';
import { formatDate } from '@/utils/date'
defineProps<{
    player: Player
}>()
</script>

<template>
    <div class='flex flex-row w-full h-fit border border-slate-600 rounded-md'>
        <div class='basis-1/3'>
            <img :src="player.image_url" />
        </div>
        <div class='basis-2/3 p-10 my-auto'>
            <div class='flex w-full'>
                <div class='flex flex-col basis-1/2 font-light text-2xl space-y-10'>
                    <p>Name</p>
                    <p>Birthday</p>
                    <p>Years Active</p>
                </div>
                <div class='flex flex-col basis-1/2 font-bold text-2xl space-y-10'>
                    <p class='truncate'>{{ player.first_name }} {{ player.last_name }}</p>
                    <p>{{ formatDate(player.birthday) }}</p>
                    <p>{{ player.start_year }} ~ {{ player.end_year || 'current' }}</p>
                </div>
            </div>
        </div>
    </div>
</template>