<script setup lang='ts'>
import MainContainer from '../layouts/MainContainer.vue'
import PlayerCard from '../components/PlayerCard.vue'
import LoadSpinner from '@/components/LoadSpinner.vue'
import { onMounted, ref } from 'vue';
import { getPlayers } from '../api'
import type { Player } from '@/types';

const players = ref<Player[]>([])
const error = ref<boolean>(false)

onMounted(async () => {
  try {
    const data = await getPlayers();
    players.value = data;
  } catch (err) {
    error.value = true
  }
})

</script>

<template>
  <MainContainer>
    <section v-if="error">
      <div class='w-full text-center text-xl space-y-5'>
        <h1>An error occurred! Please try again later</h1>
      </div>
    </section>
    <section v-else-if="players.length === 0">
      <LoadSpinner />
    </section>
    <section v-else>
      <div class='grid grid-cols-3 gap-4'>
        <PlayerCard v-for="player of players" :key="player.id" :player="player" />
      </div>
    </section>
  </MainContainer>
</template>
