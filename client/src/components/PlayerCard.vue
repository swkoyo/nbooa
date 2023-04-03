<script setup lang="ts">
import type { Player } from '../types'

defineProps<{
    player: Player
}>()
</script>

<template>
    <section>
        <div>
            <p>{{ player.first_name }}</p>
        </div>
    </section>
</template>
