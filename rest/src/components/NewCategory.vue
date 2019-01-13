<template>
  <div>
    <NavHeader></NavHeader>
    <div>
      <table class="form-group">
        <tr>
          <th>Category:</th>
          <th><input type="text" class="form-control" v-model="category"></th>
        </tr>
        <br>
        <tr>
          <th>标记 </th>
          <th>
            <select class="form-control" multiple="multiple" v-model="check_articles">
              <option :value="article.id" v-for="article in articles" :key=article.id>{{article.title}}</option>
            </select>
          </th>
        </tr>
        <br>
        <tr>
          <th>提交</th>
          <th><button class="btn btn-danger" @click="submit">submit</button></th>
        </tr>
      </table>
      <br>

    </div>
  </div>
</template>

<script>
import NavHeader from '@/components/NavHeader'
export default {
  name: 'NewCategory',
  data () {
    return {
      category: '',
      articles: '',
      check_articles: []
    }
  },
  mounted () {
    this.$axios.get('/api/articles', { headers: { 'Authorization': 'Bearer ' + this.getCookie('token') } })
      .then(response => {
        this.articles = response.data
      })
  },
  components: { NavHeader },
  methods: {
    submit: function () {
      this.$axios.post('/api/category', { 'name': this.category, 'article_ids': this.check_articles }, { headers: { 'Authorization': 'Bearer ' + this.getCookie('token') } })
        .then(response => {
          if (response.status === 200) {
            alert('新建成功')
          }
        })
    }
  }
}
</script>

<style scoped>

</style>
