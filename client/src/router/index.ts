import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import PlayersView from '../views/PlayersView.vue';
import PlayerView from '../views/PlayerView.vue';

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomeView
        },
        {
            path: '/players',
            name: 'players',
            component: PlayersView
        },
        {
            path: '/players/:_id',
            name: 'player',
            component: PlayerView,
            props: true
        }
    ]
});

export default router;
