<template>
  <div>
    <NavHeader></NavHeader>
    <div>
      <table class="form-group">
        <tr>
          <th>Title:</th>
          <th><input type="text" class="form-control"></th>
        </tr>
        <br>
        <tr>
          <th>Category:</th>
          <th>
            <select class="form-control">
              <option :value="category.id" v-for="category in categories">{{category.name}}</option>
            </select>
          </th>
        </tr>
        <br>
        <tr>
          <th>Tags:</th>
          <th>
            <select class="form-control" multiple="multiple">
              <option :value="tag.id" v-for="tag in tags">{{tag.name}}</option>
            </select>
          </th>
        </tr>
      </table>
      <br>
      <div>
        <mavon-editor :toolbars="toolbars" @save="$save"></mavon-editor>
      </div>

    </div>
  </div>
</template>

<script>
  import NavHeader from '@/components/index/NavHeader'

  export default {
    name: "NewArticle",
    data() {
      return {
        article: '',
        content: '',
        tags: '',
        categories: '',
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
    components: {NavHeader},
    mounted() {
      this.$axios.get('http://127.0.0.1:5000/api/category_titles')
        .then(response => {
          this.categories = response.data.categories
        });
      this.$axios.get('http://127.0.0.1:5000/api/tag_titles')
        .then(response => {
          this.tags = response.data.tags
        })
    },
    methods: {
      $save(content, render) {
        console.log('save success')
      }
    }
  }
</script>

<style scoped>

</style>
