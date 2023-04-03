interface Player {
    id: string;
    _id: string;
    birthday: Date;
    created_at: Date;
    start_year: string;
    end_year: string | null;
    first_name: string;
    last_name: string;
    image_url: string;
}

export const getPlayers = async () => {
    const res = await fetch(`${import.meta.env.VITE_APP_API_URL}/players`);
    if (!res.ok) throw new Error();
    const data = await res.json();
    return data as Player[];
};
