<script setup lang="ts">
import { getPlayer } from '../api'
import type { PlayerWithGameLog } from '@/types'
import { onMounted, ref } from 'vue';
import PlayerHero from '../components/PlayerHero.vue'
import MainContainer from '../layouts/MainContainer.vue'
import GameLogTable from '@/components/GameLogTable.vue'
const props = defineProps<{
    _id: string
}>()

const player = ref<PlayerWithGameLog | null>()
const isLoading = ref<boolean>(true)

onMounted(async () => {
    try {
        const data = await getPlayer(props._id);
        player.value = data;
        isLoading.value = false;
    } catch (err) {
        console.log(err)
    }
})
</script>

<template>
    <MainContainer>
        <PlayerHero v-if="player" :player="player" />
        <div v-if="player">
            <GameLogTable v-for="(gameLog, title) in player.game_logs" :key="title" :gameLog="gameLog" :title="title" />
        </div>
    </MainContainer>
</template>