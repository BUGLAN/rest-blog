<template>
  <div>
    <NavHeader></NavHeader>
    <div>
      <table class="form-group">
        <tr>
          <th>Title:</th>
          <th><input type="text" class="form-control" v-model="title" /></th>
        </tr>
        <br>
        <tr>
          <th>Slug:</th>
          <th><input type="text" class="form-control" v-model="slug" /></th>
        </tr>
        <br>
        <tr>
          <th>Category:</th>
          <th>
            <select class="form-control" v-model="check_category">
              <option :value="category.id" v-for="category in categories" :key=category.id>{{category.name}}</option>
            </select>
          </th>
        </tr>
        <br>
        <tr>
          <th>Tags:</th>
          <th>
            <select class="form-control" multiple="multiple" v-model="check_tags">
              <option :value="tag.id" v-for="tag in tags" :key=tag.id>{{tag.name}}</option>
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
import NavHeader from '@/components/NavHeader'

export default {
  name: 'NewArticle',
  data () {
    return {
      content: '',
      slug: '',
      tags: [],
      categories: '',
      check_category: '',
      check_tags: [],
      title: '',
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
        navigation: true // 导航目录
      }

    }
  },
  components: { NavHeader },
  mounted () {
    this.$axios.get(process.env.API_HOST + '/api/categories', { headers: { 'Authorization': 'Bearer ' + this.getCookie('token') } })
      .then(response => {
        this.categories = response.data
      })
    this.$axios.get(process.env.API_HOST + '/api/tags', { headers: { 'Authorization': 'Bearer ' + this.getCookie('token') } })
      .then(response => {
        this.tags = response.data
      })
  },
  methods: {
    $save (content, render) {
      this.$axios.post(process.env.API_HOST + '/api/article', {
        'title': this.title,
        'content': content,
        'slug': this.slug,
        'tag_ids': this.check_tags,
        'category_id': this.check_category
      }, { headers: { 'Authorization': 'Bearer ' + this.getCookie('token') } }).then(response => {
        if (response.status === 200) {
          alert('新建文章成功')
        } else {
          alert('新建文章失败')
        }
      })
    }
  }
}
</script>

<style scoped>

</style>
