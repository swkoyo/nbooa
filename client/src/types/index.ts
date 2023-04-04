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

export interface GameLog {
    '3P%': number;
    '3PT': string;
    AST: number;
    BLK: number;
    Date: string;
    FG: string;
    'FG%': number;
    FT: string;
    'FT%': number;
    MIN: number;
    OPP: string;
    PF: number;
    PTS: number;
    REB: number;
    RESULT: string;
    STL: number;
    TO: number;
}

export interface PlayerWithGameLog extends Player {
    game_logs: {
        birthday: GameLog | null;
        christmas: GameLog | null;
        new_years: GameLog | null;
        valentines: GameLog | null;
    };
}
