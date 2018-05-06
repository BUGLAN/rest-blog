<template>
  <div>
    <div>this is title name</div>
    <div>this a tag select box</div>
    <div>this is category</div>
    <br>
    <div>
      <mavon-editor v-model="article.content" :toolbars="toolbars" @save="$save"></mavon-editor>
    </div>

  </div>
</template>

<script>

  export default {
    name: "Editor",
    props: {
      fontSize: {
        type: String,
        default: '15px'
      }
    },
    data() {
      return {
        article: '',
        toolbars: {
          bold: true, // 粗体
          italic: true, // 斜体
          header: true, // 标题
          underline: true, // 下划线
          mark: true, // 标记
          superscript: true, // 上角标
          quote: true, // 引用
          ol: true, // 有序列表
          link: true, // 链接
          imagelink: true, // 图片链接
          help: true, // 帮助
          code: true, // code
          subfield: true, // 是否需要分栏
          fullscreen: true, // 全屏编辑
          readmodel: true, // 沉浸式阅读
          /* 1.3.5 */
          undo: true, // 上一步
          trash: true, // 清空
          save: true, // 保存（触发events中的save事件）
          /* 1.4.2 */
          navigation: true, // 导航目录
        },

      }
    },
    mounted() {
      this.$axios.get('http://127.0.0.1:5000/api/article', {params: {title: this.$route.params.name}})
        .then(response => {
          this.article = response.data.article
        })
    },
    methods: {
      $save(content, render){
        this.$axios.put('http://127.0.0.1:5000/api/article', {data: this.article})

      }
    }
  }
</script>

<style>
</style>
