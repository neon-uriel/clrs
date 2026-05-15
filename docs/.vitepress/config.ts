import { defineConfig } from 'vitepress'

export default defineConfig({
  lang: 'ja-JP',
  title: 'CLRS 講義ノート',
  description: 'CLRS に沿って学ぶアルゴリズムの講義ノート',
  cleanUrls: true,
  markdown: {
    math: true
  },
  themeConfig: {
    nav: [
      { text: 'Home', link: '/' },
      { text: '第1章', link: '/chapter-1/clrs-c1-20250511' },
      { text: '第2章', link: '/chapter-2/clrs-c2-20250511' }
    ],
    sidebar: [
      {
        text: '講義ノート',
        items: [
          { text: '第1章 アルゴリズムの役割', link: '/chapter-1/clrs-c1-20250511' },
          { text: '第2章 ソートで学ぶアルゴリズムの設計と解析', link: '/chapter-2/clrs-c2-20250511' }
        ]
      }
    ],
    outline: {
      label: 'このページ',
      level: [2, 3]
    },
    search: {
      provider: 'local'
    }
  }
})

