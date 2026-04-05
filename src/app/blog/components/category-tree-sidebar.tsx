'use client'

import { useMemo, useState } from 'react'
import { ChevronRight, X } from 'lucide-react'
import { cn } from '@/lib/utils'

type CategoryTreeSidebarProps = {
	categories: string[]
	counts: Record<string, number>
	activeCategory?: string | null
	onSelect: (category: string) => void
	onClearActive?: () => void
}

type TreeNode = {
	name: string
	path: string
	children: Map<string, TreeNode>
}

const toAnchorId = (category: string) => `cat-${encodeURIComponent(category)}`

function createNode(name: string, path: string): TreeNode {
	return { name, path, children: new Map() }
}

function buildTree(categories: string[]) {
	const root = createNode('', '')

	for (const category of categories) {
		const parts = category
			.split('/')
			.map(p => p.trim())
			.filter(Boolean)
		let current = root
		let path = ''

		for (const part of parts) {
			path = path ? `${path}/${part}` : part
			if (!current.children.has(part)) {
				current.children.set(part, createNode(part, path))
			}
			current = current.children.get(part)!
		}
	}

	return root
}

export function CategoryTreeSidebar({ categories, counts, activeCategory, onSelect, onClearActive }: CategoryTreeSidebarProps) {
	const [expanded, setExpanded] = useState<Set<string>>(() => new Set(categories.map(c => c.split('/')[0]).filter(Boolean)))

	const tree = useMemo(() => buildTree(categories), [categories])

	const isExpanded = (path: string) => expanded.has(path)

	const toggleExpand = (path: string) => {
		setExpanded(prev => {
			const next = new Set(prev)
			if (next.has(path)) next.delete(path)
			else next.add(path)
			return next
		})
	}

	const handleSelect = (category: string) => {
		onSelect(category)
		// Scroll is handled by parent component via handleCategorySelect
	}

	const renderNode = (node: TreeNode, depth = 0): React.ReactNode => {
		const hasChildren = node.children.size > 0
		const isLeaf = !hasChildren

		if (isLeaf) {
			const count = counts[node.path] ?? 0
			if (count <= 0) return null

			return (
				<button
					key={node.path}
					onClick={() => handleSelect(node.path)}
					className={cn(
						'flex w-full items-center justify-between rounded-md px-2 py-1 text-left text-sm transition-colors',
						activeCategory === node.path ? 'bg-brand/15 text-brand font-medium' : 'text-secondary hover:text-primary hover:bg-white/70'
					)}
					style={{ paddingLeft: 8 + depth * 14 }}>
					<span className='truncate'>{node.name}</span>
					<span className='text-xs tabular-nums opacity-70'>{count}</span>
				</button>
			)
		}

		const children = Array.from(node.children.values()).sort((a, b) => a.name.localeCompare(b.name, 'zh-CN'))
		const open = isExpanded(node.path)

		return (
			<div key={node.path} className='space-y-0.5'>
				<button
					onClick={() => toggleExpand(node.path)}
					className='text-primary/90 flex w-full items-center gap-1 rounded-md px-2 py-1 text-left text-sm font-medium transition-colors hover:bg-white/70'
					style={{ paddingLeft: 6 + depth * 14 }}>
					<ChevronRight className={cn('h-3.5 w-3.5 transition-transform', open && 'rotate-90')} />
					<span className='truncate'>{node.name}</span>
				</button>
				{open && <div className='space-y-0.5'>{children.map(child => renderNode(child, depth + 1))}</div>}
			</div>
		)
	}

	const roots = Array.from(tree.children.values()).sort((a, b) => a.name.localeCompare(b.name, 'zh-CN'))

	return (
		<aside className='card sticky top-[108px] mt-3 hidden max-h-[calc(100vh-200px)] w-[260px] shrink-0 p-5 lg:block'>
			<div className='mb-3 flex items-center justify-between'>
				<div className='text-sm font-semibold'>分类导航</div>
				{activeCategory && onClearActive && (
					<button onClick={onClearActive} className='text-secondary hover:text-brand p-1' aria-label='清除选中分类'>
						<X className='h-3.5 w-3.5' />
					</button>
				)}
			</div>
			<div className='max-h-[calc(100vh-252px)] overflow-auto pr-1'>
				<div className='space-y-0.5'>{roots.map(node => renderNode(node))}</div>
			</div>
		</aside>
	)
}

export const categoryToAnchorId = toAnchorId
