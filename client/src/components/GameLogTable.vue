<script setup lang="ts">
import type { GameLog } from '@/types'
defineProps<{
    title: string;
    gameLog: GameLog | null
}>()
</script>

<template>
    <h1>{{ title }}</h1>
    <thead v-if="gameLog">
        <th v-for="(_, key) in gameLog" :key="key">
            {{ key }}
        </th>
    </thead>
    <tbody v-if="gameLog">
        <tr>
            <td v-for="(value) in gameLog" :key="value">
                {{ value }}
            </td>
        </tr>
    </tbody>
    <div v-else>
        DNP
    </div>
</template>