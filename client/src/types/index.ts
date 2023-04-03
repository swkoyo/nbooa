export interface Player {
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
