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
        <th>
          <select class="form-control" v-model="check_category">
            <option value=""></option>
            <template v-for="category in categories">
              <option  :value="category.id">{{category.name}}</option>
            </template>
          </select>
        </th>
      </tr>
      <br>
      <tr>
        <th>Tags:</th>
        <th>
          <select class="form-control" multiple="multiple" v-model="check_tags">
            <template v-for="tag in tags">
              <!--<option :value="tag.id" v-for="t in article.tags" v-if="t === tag.name" selected>{{tag.name}}</option>-->
              <option :value="tag.id">{{tag.name}}</option>
            </template>

          </select>
        </th>
      </tr>
    </table>
    <br>
    <div>
      <mavon-editor ref=md v-model="article.content" :toolbars="toolbars" @save="$save"
                    @imgAdd="$imgAdd"></mavon-editor>
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
        article: [],
        tags: [],
        categories: [],
        check_category: '',
        check_tags: [],
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
         this.check_category = this.article.category.id;
          this.check_tags = this.article.tags.id;

          // let converter = new showdown.Converter()
          // this.content = converter.makeHtml(response.data.article.content)
        });
      this.$axios.get('http://127.0.0.1:5000/api/tag_titles')
        .then(response => {
          this.tags = response.data.tags
        });
      this.$axios.get('http://127.0.0.1:5000/api/category_titles')
        .then(response => {
          this.categories = response.data.categories
        });
    },
    methods: {
      $save(content, render) {
        this.$axios.put('http://127.0.0.1:5000/api/article', {
          title: this.article.title,
          content: content,
          id: this.article.id,
          category: this.check_category,
          tags: this.check_tags
        })
          .then(response => {
            if (response.status === 200) {
              alert('保存成功')
            } else {
              alert('保存失败')
            }
          })

      },
      $imgAdd(pos, $file) {
        // 第一步.将图片上传到服务器.
        let formdata = new FormData();
        formdata.append('image', $file);
        this.$axios({
          url: 'http://127.0.0.1:5000/api/upload_image',
          method: 'post',
          data: formdata,
          headers: {'Content-Type': 'multipart/form-data'},
        }).then(response => {
          // 第二步.将返回的url替换到文本原位置![...](./0) -> ![...](url)
          if (response.status === 200) {
            this.$refs.md.$img2Url(pos, response.data.url);
          } else {
            alert('上传图片失败')
          }

        })
      },
    },

  }
</script>

<style>
</style>
