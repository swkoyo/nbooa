import type { Player } from '../types';

export const getPlayers = async () => {
    const res = await fetch(`${import.meta.env.VITE_APP_API_URL}/players`);
    if (!res.ok) throw new Error();
    const data = await res.json();
    return data as Player[];
};
