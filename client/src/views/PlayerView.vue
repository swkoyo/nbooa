<script setup lang="ts">
import { getPlayer } from '../api'
import type { PlayerWithGameLog } from '@/types'
import { onMounted, ref } from 'vue';
import PlayerHero from '../components/PlayerHero.vue'
import MainContainer from '../layouts/MainContainer.vue'
import GameLogTable from '@/components/GameLogTable.vue'
import LoadSpinner from '@/components/LoadSpinner.vue'
const props = defineProps<{
    _id: string
}>()

const player = ref<PlayerWithGameLog | null>()

onMounted(async () => {
    try {
        const data = await getPlayer(props._id);
        player.value = data;
    } catch (err) {
        console.log(err)
    }
})
</script>

<template>
    <MainContainer>
        <section v-if="!player">
            <LoadSpinner />
        </section>
        <section v-else>
            <PlayerHero :player="player" />
            <div class='space-y-4'>
                <GameLogTable v-for="(gameLog, title) in player.game_logs" :key="title" :gameLog="gameLog" :title="title" />
            </div>
        </section>
    </MainContainer>
</template>