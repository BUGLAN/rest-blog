<template>
  <div>
    <NavHeader></NavHeader>
    <div>
      <table class="form-group">
        <tr>
          <th>Tag:</th>
          <th><input type="text" class="form-control" v-model="tag"></th>
        </tr>
        <br>
        <tr>
          <th>标记为 {{tag}}</th>
          <th>
            <select class="form-control" multiple="multiple" >
              <option :value="article.id" v-for="article in articles">{{article.title}}</option>
            </select>
          </th>
        </tr>
        <br>
        <tr>
          <th>提交</th>
          <th>
            <button class="btn btn-danger">submit</button>
          </th>
        </tr>
      </table>
      <br>

    </div>
  </div>
</template>

<script>
  import NavHeader from '@/components/index/NavHeader'

  export default {
    name: "NewTag",
    data(){
      return {
        tag: '',
        articles: ''
      }
    },
    mounted(){
      this.$axios.get('http://127.0.0.1:5000/api/article_titles')
        .then(response => {
          this.articles = response.data.articles
        })
    },
    components: {NavHeader}
  }
</script>

<style scoped>

</style>
