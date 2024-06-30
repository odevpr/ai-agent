'use client'

import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { ReactQueryDevtools } from '@tanstack/react-query-devtools'
import { useState, ReactNode } from 'react'
import { ChatProvider } from '@/context/ChatProvider'

const ONE_DAY_IN_MS = 1000 * 60 * 60 * 24

export function AppProvider({ children }: { children: ReactNode }) {
    const [queryClient] = useState(() => new QueryClient({
        defaultOptions: {
            queries: {
                staleTime: ONE_DAY_IN_MS,
                gcTime: ONE_DAY_IN_MS,
            },
        },
    }))

    return (
        <QueryClientProvider client={queryClient}>
            <ChatProvider>
                {children}
            </ChatProvider>
            <ReactQueryDevtools initialIsOpen={false} />
        </QueryClientProvider>
    )
}