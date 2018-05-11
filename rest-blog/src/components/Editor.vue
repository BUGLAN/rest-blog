<template>
  <div>
    <table class="form-group">
      <tr>
        <th>Title:</th>
        <th><input type="text" class="form-control" v-model="article.title"></th>
      </tr>
      <br>
      <tr>
        <th>Category:</th>
        <th><input type="text" class="form-control" v-model="article.category"></th>
      </tr>
      <br>
      <tr>
        <th>Tags:</th>
        <th>
          <select class="form-control" multiple="multiple" >
            <option selected>Open this select menu</option>
            <option selected>One</option>
            <option value="2">Two</option>
            <option value="3">Three</option>
            <option value="4">WoCao</option>
            <option value="2">Two</option>
            <option value="3">Three</option>
            <option value="4">Flask</option>
            <option value="2">Two</option>
            <option value="3">Three</option>
            <option value="4">None</option>
          </select>
        </th>
      </tr>
    </table>
    <br>
    <div>
      <mavon-editor v-model="article.content" :toolbars="toolbars" @save="$save"></mavon-editor>
    </div>

  </div>
</template>

<script>
  import showdown from 'showdown'

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
        content: '',
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
          this.article = response.data.article;
          let converter = new showdown.Converter()
          this.content = converter.makeHtml(response.data.article.content)

        })
    },
    methods: {
      $save(content, render) {
        this.$axios.put('http://127.0.0.1:5000/api/article', {data: content, id: this.article.id})

      }
    }
  }
</script>

<style>
</style>
