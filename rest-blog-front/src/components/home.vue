<!--<template>-->
  <!--<div id="app">-->
    <!--<headerDiv logo="Wise"></headerDiv>-->
    <!--<router-view></router-view>-->
    <!--<footerDiv></footerDiv>-->
  <!--</div>-->
<!--</template>-->

<template>
  <header class="header"></header>
  <ul class="nav">
    <li v-for="nav in navs">
      <router-link to="nav.method">{{nav.title}}</router-link>
    </li>
  </ul>
</template>
