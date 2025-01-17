"use client"
import { type ClassValue, clsx } from "clsx"
import { twMerge } from "tailwind-merge"
import { v4 as uuidv4 } from 'uuid'

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

export function makeId(prefix: string): string {
  return `${prefix}-${uuidv4()}`;
}

export function formatUglyDate(dateStr: string): string {
  const year = parseInt(dateStr.slice(0, 4));
  const month = parseInt(dateStr.slice(4, 6)) - 1;
  const day = parseInt(dateStr.slice(6, 8));

  const date = new Date(Date.UTC(year, month, day));

  return date.toISOString().split('T')[0];
}
