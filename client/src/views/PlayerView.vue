<script setup lang="ts">
import { getPlayer } from '../api'
import type { PlayerWithGameLog } from '@/types'
import { onMounted, ref } from 'vue';
import PlayerHero from '../components/PlayerHero.vue'
import MainContainer from '../layouts/MainContainer.vue'
import GameLogTable from '@/components/GameLogTable.vue'
import LoadSpinner from '@/components/LoadSpinner.vue'
import router from '@/router';
const props = defineProps<{
    _id: string
}>()

const player = ref<PlayerWithGameLog | null>()
const error = ref<boolean>(false)

onMounted(async () => {
    try {
        const data = await getPlayer(props._id);
        player.value = data;
    } catch (err) {
        error.value = true
    }
})
</script>

<template>
    <MainContainer>
        <section v-if="error">
            <div class='w-full text-center text-xl space-y-5'>
                <h1>An error occured!</h1>
                <button @click="router.replace('/players')"
                    class='bg-indigo-500 rounded-full text-sm px-3 py-2 hover:bg-opacity-50'>Go
                    back</button>
            </div>
        </section>
        <section v-else-if="!player">
            <LoadSpinner />
        </section>
        <section v-else>
            <PlayerHero :player="player" />
            <div class='space-y-4 pt-10'>
                <GameLogTable v-for="(gameLog, title) in player.game_logs" :key="title" :gameLog="gameLog" :title="title" />
            </div>
        </section>
    </MainContainer>
</template>