'use client'

import { useMemo } from 'react'
import { X } from 'lucide-react'
import { cn } from '@/lib/utils'

type CategoryTreeSidebarProps = {
	categories: string[]
	counts: Record<string, number>
	activeCategory?: string | null
	onSelect: (category: string) => void
	onClearActive?: () => void
}

const toAnchorId = (category: string) => `cat-${encodeURIComponent(category)}`

export function CategoryTreeSidebar({ categories, counts, activeCategory, onSelect, onClearActive }: CategoryTreeSidebarProps) {
	const handleSelect = (category: string) => {
		onSelect(category)
	}

	// 只显示有文章的分类，保持与主列表一致的顺序
	const visibleCategories = useMemo(() => {
		return categories.filter(cat => (counts[cat] ?? 0) > 0)
	}, [categories, counts])

	return (
		<aside className='card sticky top-[108px] mt-3 hidden max-h-[calc(100vh-200px)] w-[260px] shrink-0 flex-col overflow-hidden p-5 lg:flex'>
			<div className='mb-3 flex shrink-0 items-center justify-between'>
				<div className='text-sm font-semibold'>分类导航</div>
				{activeCategory && onClearActive && (
					<button onClick={onClearActive} className='text-secondary hover:text-brand p-1' aria-label='清除选中分类'>
						<X className='h-3.5 w-3.5' />
					</button>
				)}
			</div>
			{/* 添加滚动条：当分类过多时可以滚动 */}
			<div className='scrollbar-custom min-h-0 flex-1 overflow-y-auto pr-1'>
				<div className='space-y-0.5'>
					{visibleCategories.map(category => {
						const count = counts[category] ?? 0
						return (
							<button
								key={category}
								onClick={() => handleSelect(category)}
								className={cn(
									'flex w-full items-center justify-between rounded-md px-3 py-2 text-left text-sm transition-colors',
									activeCategory === category ? 'bg-brand/15 text-brand font-medium' : 'text-secondary hover:text-primary hover:bg-white/70'
								)}>
								<span className='truncate'>{category}</span>
								<span className='text-xs tabular-nums opacity-70'>{count}</span>
							</button>
						)
					})}
				</div>
			</div>
		</aside>
	)
}

export const categoryToAnchorId = toAnchorId
