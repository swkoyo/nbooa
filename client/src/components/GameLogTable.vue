<script setup lang="ts">
import type { GameLog } from '@/types'
import { TABLE_KEYS } from '@/constants'
import { startCase } from 'lodash'
defineProps<{
    title: string;
    gameLog: GameLog | null
}>()
</script>

<template>
    <div class='inline-block min-w-full bg-white p-4 rounded-md shadow-md'>
        <h1 class='text-xl'>{{ startCase(title) }}</h1>
        <table class='table-auto min-w-full text-left font-light text-xs'>
            <thead class='border-b font-medium'>
                <tr>
                    <th v-for="key of TABLE_KEYS" :key="key" class='px-2 py-4'>
                        {{ key }}
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr v-if="gameLog" class='border-b'>
                    <td v-for="key of TABLE_KEYS" :key="key" class='px-2 py-4'>
                        {{ gameLog[key] }}
                    </td>
                </tr>
                <tr v-else class='border-b'>
                    <td v-for="key of TABLE_KEYS" :key="key" class='px-2 py-4'>
                        -
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>