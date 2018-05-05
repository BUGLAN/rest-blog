var header_nav = Vue.component('header-nav', {
    template: '<header id="top">\n' +
    '    <ul>\n' +
    '        <li><a href="" class="no-botterm"><img src="/static/icons/home.svg" alt="">Home</a></li>\n' +
    '        <li><a href="" class="no-botterm"><img src="/static/icons/archive.svg" alt="">Axis</a></li>\n' +
    '        <li><a href="" class="no-botterm"><img src="/static/icons/tags.svg" alt="">Tags</a></li>\n' +
    '        <li><a href="" class="no-botterm"><img src="/static/icons/about.svg" alt="">About</a></li>\n' +
    '        <li><a href="" class="no-botterm"><img src="/static/icons/github.svg" alt="">Github</a></li>\n' +
    '\n' +
    '    </ul>\n' +
    '</header>'
})

const app = new Vue({
    el: '#header',
})


var datas = new Vue({
    el: "#app1",
    data: {
        items: [
            {
                'title': '代码编辑器系列',
                'article': '在看了那么久 IntelliJ IDEA 的架构后，自己心里总是痒痒的，想自己实现一个差不多的文本编辑器。\n' +
                '                    现在基础设施已经差不多全了（补全、基于 Parser 的带语义分析的和基于 Lexer 的基于 Token 的高亮、插件系统、撤销-重做系统），\n' +
                '                    华而不实的东西也做了一些（拖放打开文件、背景图片、可以热更新的设置、自定义字体、 AST 阅读器（即 PsiViewer），还有一个初中小朋友写的查找替换、多行注释/取消注释等），\n' +
                '                    项目叫 DevKt ，代码在这里，可以直接在 release 里面下载试用。\n' +
                '\n' +
                '                    在做了这个文本编辑器之后，我又学到了很...',
                'date': '2018/04/27'
            },
            {
                'title': '代码编辑器系列 &num;0 两种编辑器',
                'article': '在看了那么久 IntelliJ IDEA 的架构后，自己心里总是痒痒的，想自己实现一个差不多的文本编辑器。\n' +
                '                    现在基础设施已经差不多全了（补全、基于 Parser 的带语义分析的和基于 Lexer 的基于 Token 的高亮、插件系统、撤销-重做系统），\n' +
                '                    华而不实的东西也做了一些（拖放打开文件、背景图片、可以热更新的设置、自定义字体、 AST 阅读器（即 PsiViewer），还有一个初中小朋友写的查找替换、多行注释/取消注释等），\n' +
                '                    项目叫 DevKt ，代码在这里，可以直接在 release 里面下载试用。\n' +
                '\n' +
                '                    在做了这个文本编辑器之后，我又学到了很...',
                'date': '2018/04/27'
            },
            {
                'title': '代码编辑器系列 &num;0 两种编辑器',
                'article': '在看了那么久 IntelliJ IDEA 的架构后，自己心里总是痒痒的，想自己实现一个差不多的文本编辑器。\n' +
                '                    现在基础设施已经差不多全了（补全、基于 Parser 的带语义分析的和基于 Lexer 的基于 Token 的高亮、插件系统、撤销-重做系统），\n' +
                '                    华而不实的东西也做了一些（拖放打开文件、背景图片、可以热更新的设置、自定义字体、 AST 阅读器（即 PsiViewer），还有一个初中小朋友写的查找替换、多行注释/取消注释等），\n' +
                '                    项目叫 DevKt ，代码在这里，可以直接在 release 里面下载试用。\n' +
                '\n' +
                '                    在做了这个文本编辑器之后，我又学到了很...',
                'date': '2018/04/27'
            },
            {
                'title': '代码编辑器系列 &num;0 两种编辑器',
                'article': '在看了那么久 IntelliJ IDEA 的架构后，自己心里总是痒痒的，想自己实现一个差不多的文本编辑器。\n' +
                '                    现在基础设施已经差不多全了（补全、基于 Parser 的带语义分析的和基于 Lexer 的基于 Token 的高亮、插件系统、撤销-重做系统），\n' +
                '                    华而不实的东西也做了一些（拖放打开文件、背景图片、可以热更新的设置、自定义字体、 AST 阅读器（即 PsiViewer），还有一个初中小朋友写的查找替换、多行注释/取消注释等），\n' +
                '                    项目叫 DevKt ，代码在这里，可以直接在 release 里面下载试用。\n' +
                '\n' +
                '                    在做了这个文本编辑器之后，我又学到了很...',
                'date': '2018/04/27'
            },
            {
                'title': '代码编辑器系列 &num;0 两种编辑器',
                'article': '在看了那么久 IntelliJ IDEA 的架构后，自己心里总是痒痒的，想自己实现一个差不多的文本编辑器。\n' +
                '                    现在基础设施已经差不多全了（补全、基于 Parser 的带语义分析的和基于 Lexer 的基于 Token 的高亮、插件系统、撤销-重做系统），\n' +
                '                    华而不实的东西也做了一些（拖放打开文件、背景图片、可以热更新的设置、自定义字体、 AST 阅读器（即 PsiViewer），还有一个初中小朋友写的查找替换、多行注释/取消注释等），\n' +
                '                    项目叫 DevKt ，代码在这里，可以直接在 release 里面下载试用。\n' +
                '\n' +
                '                    在做了这个文本编辑器之后，我又学到了很...',
                'date': '2018/04/27'
            },
        ]
    },
    components: {
        'my-article': {
            props: ['items'],
            template: '<section id="articles">\n' +
            '<ul>\n' +
            '        <li v-for="item in items">\n' +
            '            <article>\n' +
            '                <h1>\n' +
            '                    <a href="/2018/04/27/CodeEditor/" title="代码编辑器系列 &num;0 两种编辑器">{{item.title}}</a>\n' +
            '                </h1>\n' +
            '                <p>{{item.date}}</p>\n' +
            '                <div class="content"><p>{{item.article}}</p></div>\n' +
            '                <p><a href="">Editor</a></p>\n' +
            '            </article>\n' +
            '        </li>\n' +
            '</ul>\n' +
            '</section>'
        }

    }
});


Vue.component('my-footer', {
    props: ['pages'],
    template: '<nav>\n' +
    '    <h1>\n' +
    '        <a href="" v-for="page in pages">{{page}}\n</a>' +
    '    </h1>\n' +
    '</nav>'
})

var footers = new Vue({
    el: '#my-footer',
    data: {
        pages: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    },

})

