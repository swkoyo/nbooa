import type { Player, PlayerWithGameLog } from '../types';

export const getPlayers = async () => {
    const res = await fetch(`${import.meta.env.VITE_APP_API_URL}/players`);
    if (!res.ok) throw new Error();
    const data = await res.json();
    return data as Player[];
};

export const getPlayer = async (_id: string) => {
    const res = await fetch(`${import.meta.env.VITE_APP_API_URL}/players/${_id}`);
    const data = await res.json();
    if (!res.ok) throw new Error(data);
    return data as PlayerWithGameLog;
};
