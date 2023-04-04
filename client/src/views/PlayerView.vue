<script setup lang="ts">
import { getPlayer } from '../api'
import type { PlayerWithGameLog } from '@/types'
import { onMounted, ref } from 'vue';
import MainContainer from '../layouts/MainContainer.vue'
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
        {{ player }}
    </MainContainer>
</template>