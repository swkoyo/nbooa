import type { GameLog } from './types';

export const API_URL = import.meta.env.VITE_APP_API_URL;
export const TABLE_KEYS: (keyof GameLog)[] = [
    'Date',
    'OPP',
    'Result',
    'MIN',
    'FG',
    'FG%',
    '3PT',
    '3P%',
    'FT',
    'FT%',
    'REB',
    'AST',
    'BLK',
    'STL',
    'PF',
    'TO',
    'PTS'
];
