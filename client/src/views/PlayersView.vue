<script setup lang='ts'>
import MainContainer from '../layouts/MainContainer.vue'
import PlayerCard from '../components/PlayerCard.vue'
import { onMounted, ref } from 'vue';
import { getPlayers } from '../api'
import type { Player } from '@/types';

const players = ref<Player[]>([])

onMounted(async () => {
  try {
    const data = await getPlayers();
    players.value = data;
  } catch (err) {
    console.log(err)
  }
})

</script>

<template>
  <MainContainer>
    <section>
      <p>Players</p>
      <div class='grid grid-cols-4 gap-4'>
        <PlayerCard v-for="player in players" :key="player.id" :player="player" />
      </div>
    </section>
  </MainContainer>
</template>
