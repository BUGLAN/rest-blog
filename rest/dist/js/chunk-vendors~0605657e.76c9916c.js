(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-vendors~0605657e"],{2877:function(t,e,r){"use strict";function n(t,e,r,n,o,i,a,u){var c,s="function"===typeof t?t.options:t;if(e&&(s.render=e,s.staticRenderFns=r,s._compiled=!0),n&&(s.functional=!0),i&&(s._scopeId="data-v-"+i),a?(c=function(t){t=t||this.$vnode&&this.$vnode.ssrContext||this.parent&&this.parent.$vnode&&this.parent.$vnode.ssrContext,t||"undefined"===typeof __VUE_SSR_CONTEXT__||(t=__VUE_SSR_CONTEXT__),o&&o.call(this,t),t&&t._registeredComponents&&t._registeredComponents.add(a)},s._ssrRegister=c):o&&(c=u?function(){o.call(this,this.$root.$options.shadowRoot)}:o),c)if(s.functional){s._injectStyles=c;var p=s.render;s.render=function(t,e){return c.call(e),p(t,e)}}else{var f=s.beforeCreate;s.beforeCreate=f?[].concat(f,c):[c]}return{exports:t,options:s}}r.d(e,"a",function(){return n})},"8c4f":function(t,e,r){"use strict";
/*!
  * vue-router v3.0.2
  * (c) 2018 Evan You
  * @license MIT
  */function n(t,e){0}function o(t){return Object.prototype.toString.call(t).indexOf("Error")>-1}function i(t,e){for(var r in e)t[r]=e[r];return t}var a={name:"RouterView",functional:!0,props:{name:{type:String,default:"default"}},render:function(t,e){var r=e.props,n=e.children,o=e.parent,a=e.data;a.routerView=!0;var c=o.$createElement,s=r.name,p=o.$route,f=o._routerViewCache||(o._routerViewCache={}),h=0,l=!1;while(o&&o._routerRoot!==o)o.$vnode&&o.$vnode.data.routerView&&h++,o._inactive&&(l=!0),o=o.$parent;if(a.routerViewDepth=h,l)return c(f[s],a,n);var d=p.matched[h];if(!d)return f[s]=null,c();var v=f[s]=d.components[s];a.registerRouteInstance=function(t,e){var r=d.instances[s];(e&&r!==t||!e&&r===t)&&(d.instances[s]=e)},(a.hook||(a.hook={})).prepatch=function(t,e){d.instances[s]=e.componentInstance};var y=a.props=u(p,d.props&&d.props[s]);if(y){y=a.props=i({},y);var m=a.attrs=a.attrs||{};for(var g in y)v.props&&g in v.props||(m[g]=y[g],delete y[g])}return c(v,a,n)}};function u(t,e){switch(typeof e){case"undefined":return;case"object":return e;case"function":return e(t);case"boolean":return e?t.params:void 0;default:0}}var c=/[!'()*]/g,s=function(t){return"%"+t.charCodeAt(0).toString(16)},p=/%2C/g,f=function(t){return encodeURIComponent(t).replace(c,s).replace(p,",")},h=decodeURIComponent;function l(t,e,r){void 0===e&&(e={});var n,o=r||d;try{n=o(t||"")}catch(a){n={}}for(var i in e)n[i]=e[i];return n}function d(t){var e={};return t=t.trim().replace(/^(\?|#|&)/,""),t?(t.split("&").forEach(function(t){var r=t.replace(/\+/g," ").split("="),n=h(r.shift()),o=r.length>0?h(r.join("=")):null;void 0===e[n]?e[n]=o:Array.isArray(e[n])?e[n].push(o):e[n]=[e[n],o]}),e):e}function v(t){var e=t?Object.keys(t).map(function(e){var r=t[e];if(void 0===r)return"";if(null===r)return f(e);if(Array.isArray(r)){var n=[];return r.forEach(function(t){void 0!==t&&(null===t?n.push(f(e)):n.push(f(e)+"="+f(t)))}),n.join("&")}return f(e)+"="+f(r)}).filter(function(t){return t.length>0}).join("&"):null;return e?"?"+e:""}var y=/\/?$/;function m(t,e,r,n){var o=n&&n.options.stringifyQuery,i=e.query||{};try{i=g(i)}catch(u){}var a={name:e.name||t&&t.name,meta:t&&t.meta||{},path:e.path||"/",hash:e.hash||"",query:i,params:e.params||{},fullPath:x(e,o),matched:t?b(t):[]};return r&&(a.redirectedFrom=x(r,o)),Object.freeze(a)}function g(t){if(Array.isArray(t))return t.map(g);if(t&&"object"===typeof t){var e={};for(var r in t)e[r]=g(t[r]);return e}return t}var w=m(null,{path:"/"});function b(t){var e=[];while(t)e.unshift(t),t=t.parent;return e}function x(t,e){var r=t.path,n=t.query;void 0===n&&(n={});var o=t.hash;void 0===o&&(o="");var i=e||v;return(r||"/")+i(n)+o}function k(t,e){return e===w?t===e:!!e&&(t.path&&e.path?t.path.replace(y,"")===e.path.replace(y,"")&&t.hash===e.hash&&R(t.query,e.query):!(!t.name||!e.name)&&(t.name===e.name&&t.hash===e.hash&&R(t.query,e.query)&&R(t.params,e.params)))}function R(t,e){if(void 0===t&&(t={}),void 0===e&&(e={}),!t||!e)return t===e;var r=Object.keys(t),n=Object.keys(e);return r.length===n.length&&r.every(function(r){var n=t[r],o=e[r];return"object"===typeof n&&"object"===typeof o?R(n,o):String(n)===String(o)})}function _(t,e){return 0===t.path.replace(y,"/").indexOf(e.path.replace(y,"/"))&&(!e.hash||t.hash===e.hash)&&E(t.query,e.query)}function E(t,e){for(var r in e)if(!(r in t))return!1;return!0}var C,O=[String,Object],j=[String,Array],A={name:"RouterLink",props:{to:{type:O,required:!0},tag:{type:String,default:"a"},exact:Boolean,append:Boolean,replace:Boolean,activeClass:String,exactActiveClass:String,event:{type:j,default:"click"}},render:function(t){var e=this,r=this.$router,n=this.$route,o=r.resolve(this.to,n,this.append),a=o.location,u=o.route,c=o.href,s={},p=r.options.linkActiveClass,f=r.options.linkExactActiveClass,h=null==p?"router-link-active":p,l=null==f?"router-link-exact-active":f,d=null==this.activeClass?h:this.activeClass,v=null==this.exactActiveClass?l:this.exactActiveClass,y=a.path?m(null,a,null,r):u;s[v]=k(n,y),s[d]=this.exact?s[v]:_(n,y);var g=function(t){T(t)&&(e.replace?r.replace(a):r.push(a))},w={click:T};Array.isArray(this.event)?this.event.forEach(function(t){w[t]=g}):w[this.event]=g;var b={class:s};if("a"===this.tag)b.on=w,b.attrs={href:c};else{var x=S(this.$slots.default);if(x){x.isStatic=!1;var R=x.data=i({},x.data);R.on=w;var E=x.data.attrs=i({},x.data.attrs);E.href=c}else b.on=w}return t(this.tag,b,this.$slots.default)}};function T(t){if(!(t.metaKey||t.altKey||t.ctrlKey||t.shiftKey)&&!t.defaultPrevented&&(void 0===t.button||0===t.button)){if(t.currentTarget&&t.currentTarget.getAttribute){var e=t.currentTarget.getAttribute("target");if(/\b_blank\b/i.test(e))return}return t.preventDefault&&t.preventDefault(),!0}}function S(t){if(t)for(var e,r=0;r<t.length;r++){if(e=t[r],"a"===e.tag)return e;if(e.children&&(e=S(e.children)))return e}}function $(t){if(!$.installed||C!==t){$.installed=!0,C=t;var e=function(t){return void 0!==t},r=function(t,r){var n=t.$options._parentVnode;e(n)&&e(n=n.data)&&e(n=n.registerRouteInstance)&&n(t,r)};t.mixin({beforeCreate:function(){e(this.$options.router)?(this._routerRoot=this,this._router=this.$options.router,this._router.init(this),t.util.defineReactive(this,"_route",this._router.history.current)):this._routerRoot=this.$parent&&this.$parent._routerRoot||this,r(this,this)},destroyed:function(){r(this)}}),Object.defineProperty(t.prototype,"$router",{get:function(){return this._routerRoot._router}}),Object.defineProperty(t.prototype,"$route",{get:function(){return this._routerRoot._route}}),t.component("RouterView",a),t.component("RouterLink",A);var n=t.config.optionMergeStrategies;n.beforeRouteEnter=n.beforeRouteLeave=n.beforeRouteUpdate=n.created}}var L="undefined"!==typeof window;function q(t,e,r){var n=t.charAt(0);if("/"===n)return t;if("?"===n||"#"===n)return e+t;var o=e.split("/");r&&o[o.length-1]||o.pop();for(var i=t.replace(/^\//,"").split("/"),a=0;a<i.length;a++){var u=i[a];".."===u?o.pop():"."!==u&&o.push(u)}return""!==o[0]&&o.unshift(""),o.join("/")}function U(t){var e="",r="",n=t.indexOf("#");n>=0&&(e=t.slice(n),t=t.slice(0,n));var o=t.indexOf("?");return o>=0&&(r=t.slice(o+1),t=t.slice(0,o)),{path:t,query:r,hash:e}}function P(t){return t.replace(/\/\//g,"/")}var I=Array.isArray||function(t){return"[object Array]"==Object.prototype.toString.call(t)},V=nt,M=D,B=J,H=X,z=rt,F=new RegExp(["(\\\\.)","([\\/.])?(?:(?:\\:(\\w+)(?:\\(((?:\\\\.|[^\\\\()])+)\\))?|\\(((?:\\\\.|[^\\\\()])+)\\))([+*?])?|(\\*))"].join("|"),"g");function D(t,e){var r,n=[],o=0,i=0,a="",u=e&&e.delimiter||"/";while(null!=(r=F.exec(t))){var c=r[0],s=r[1],p=r.index;if(a+=t.slice(i,p),i=p+c.length,s)a+=s[1];else{var f=t[i],h=r[2],l=r[3],d=r[4],v=r[5],y=r[6],m=r[7];a&&(n.push(a),a="");var g=null!=h&&null!=f&&f!==h,w="+"===y||"*"===y,b="?"===y||"*"===y,x=r[2]||u,k=d||v;n.push({name:l||o++,prefix:h||"",delimiter:x,optional:b,repeat:w,partial:g,asterisk:!!m,pattern:k?Y(k):m?".*":"[^"+Q(x)+"]+?"})}}return i<t.length&&(a+=t.substr(i)),a&&n.push(a),n}function J(t,e){return X(D(t,e))}function K(t){return encodeURI(t).replace(/[\/?#]/g,function(t){return"%"+t.charCodeAt(0).toString(16).toUpperCase()})}function N(t){return encodeURI(t).replace(/[?#]/g,function(t){return"%"+t.charCodeAt(0).toString(16).toUpperCase()})}function X(t){for(var e=new Array(t.length),r=0;r<t.length;r++)"object"===typeof t[r]&&(e[r]=new RegExp("^(?:"+t[r].pattern+")$"));return function(r,n){for(var o="",i=r||{},a=n||{},u=a.pretty?K:encodeURIComponent,c=0;c<t.length;c++){var s=t[c];if("string"!==typeof s){var p,f=i[s.name];if(null==f){if(s.optional){s.partial&&(o+=s.prefix);continue}throw new TypeError('Expected "'+s.name+'" to be defined')}if(I(f)){if(!s.repeat)throw new TypeError('Expected "'+s.name+'" to not repeat, but received `'+JSON.stringify(f)+"`");if(0===f.length){if(s.optional)continue;throw new TypeError('Expected "'+s.name+'" to not be empty')}for(var h=0;h<f.length;h++){if(p=u(f[h]),!e[c].test(p))throw new TypeError('Expected all "'+s.name+'" to match "'+s.pattern+'", but received `'+JSON.stringify(p)+"`");o+=(0===h?s.prefix:s.delimiter)+p}}else{if(p=s.asterisk?N(f):u(f),!e[c].test(p))throw new TypeError('Expected "'+s.name+'" to match "'+s.pattern+'", but received "'+p+'"');o+=s.prefix+p}}else o+=s}return o}}function Q(t){return t.replace(/([.+*?=^!:${}()[\]|\/\\])/g,"\\$1")}function Y(t){return t.replace(/([=!:$\/()])/g,"\\$1")}function W(t,e){return t.keys=e,t}function G(t){return t.sensitive?"":"i"}function Z(t,e){var r=t.source.match(/\((?!\?)/g);if(r)for(var n=0;n<r.length;n++)e.push({name:n,prefix:null,delimiter:null,optional:!1,repeat:!1,partial:!1,asterisk:!1,pattern:null});return W(t,e)}function tt(t,e,r){for(var n=[],o=0;o<t.length;o++)n.push(nt(t[o],e,r).source);var i=new RegExp("(?:"+n.join("|")+")",G(r));return W(i,e)}function et(t,e,r){return rt(D(t,r),e,r)}function rt(t,e,r){I(e)||(r=e||r,e=[]),r=r||{};for(var n=r.strict,o=!1!==r.end,i="",a=0;a<t.length;a++){var u=t[a];if("string"===typeof u)i+=Q(u);else{var c=Q(u.prefix),s="(?:"+u.pattern+")";e.push(u),u.repeat&&(s+="(?:"+c+s+")*"),s=u.optional?u.partial?c+"("+s+")?":"(?:"+c+"("+s+"))?":c+"("+s+")",i+=s}}var p=Q(r.delimiter||"/"),f=i.slice(-p.length)===p;return n||(i=(f?i.slice(0,-p.length):i)+"(?:"+p+"(?=$))?"),i+=o?"$":n&&f?"":"(?="+p+"|$)",W(new RegExp("^"+i,G(r)),e)}function nt(t,e,r){return I(e)||(r=e||r,e=[]),r=r||{},t instanceof RegExp?Z(t,e):I(t)?tt(t,e,r):et(t,e,r)}V.parse=M,V.compile=B,V.tokensToFunction=H,V.tokensToRegExp=z;var ot=Object.create(null);function it(t,e,r){try{var n=ot[t]||(ot[t]=V.compile(t));return n(e||{},{pretty:!0})}catch(o){return""}}function at(t,e,r,n){var o=e||[],i=r||Object.create(null),a=n||Object.create(null);t.forEach(function(t){ut(o,i,a,t)});for(var u=0,c=o.length;u<c;u++)"*"===o[u]&&(o.push(o.splice(u,1)[0]),c--,u--);return{pathList:o,pathMap:i,nameMap:a}}function ut(t,e,r,n,o,i){var a=n.path,u=n.name;var c=n.pathToRegexpOptions||{},s=st(a,o,c.strict);"boolean"===typeof n.caseSensitive&&(c.sensitive=n.caseSensitive);var p={path:s,regex:ct(s,c),components:n.components||{default:n.component},instances:{},name:u,parent:o,matchAs:i,redirect:n.redirect,beforeEnter:n.beforeEnter,meta:n.meta||{},props:null==n.props?{}:n.components?n.props:{default:n.props}};if(n.children&&n.children.forEach(function(n){var o=i?P(i+"/"+n.path):void 0;ut(t,e,r,n,p,o)}),void 0!==n.alias){var f=Array.isArray(n.alias)?n.alias:[n.alias];f.forEach(function(i){var a={path:i,children:n.children};ut(t,e,r,a,o,p.path||"/")})}e[p.path]||(t.push(p.path),e[p.path]=p),u&&(r[u]||(r[u]=p))}function ct(t,e){var r=V(t,[],e);return r}function st(t,e,r){return r||(t=t.replace(/\/$/,"")),"/"===t[0]?t:null==e?t:P(e.path+"/"+t)}function pt(t,e,r,n){var o="string"===typeof t?{path:t}:t;if(o.name||o._normalized)return o;if(!o.path&&o.params&&e){o=i({},o),o._normalized=!0;var a=i(i({},e.params),o.params);if(e.name)o.name=e.name,o.params=a;else if(e.matched.length){var u=e.matched[e.matched.length-1].path;o.path=it(u,a,"path "+e.path)}else 0;return o}var c=U(o.path||""),s=e&&e.path||"/",p=c.path?q(c.path,s,r||o.append):s,f=l(c.query,o.query,n&&n.options.parseQuery),h=o.hash||c.hash;return h&&"#"!==h.charAt(0)&&(h="#"+h),{_normalized:!0,path:p,query:f,hash:h}}function ft(t,e){var r=at(t),n=r.pathList,o=r.pathMap,i=r.nameMap;function a(t){at(t,n,o,i)}function u(t,r,a){var u=pt(t,r,!1,e),c=u.name;if(c){var s=i[c];if(!s)return p(null,u);var f=s.regex.keys.filter(function(t){return!t.optional}).map(function(t){return t.name});if("object"!==typeof u.params&&(u.params={}),r&&"object"===typeof r.params)for(var h in r.params)!(h in u.params)&&f.indexOf(h)>-1&&(u.params[h]=r.params[h]);if(s)return u.path=it(s.path,u.params,'named route "'+c+'"'),p(s,u,a)}else if(u.path){u.params={};for(var l=0;l<n.length;l++){var d=n[l],v=o[d];if(ht(v.regex,u.path,u.params))return p(v,u,a)}}return p(null,u)}function c(t,r){var n=t.redirect,o="function"===typeof n?n(m(t,r,null,e)):n;if("string"===typeof o&&(o={path:o}),!o||"object"!==typeof o)return p(null,r);var a=o,c=a.name,s=a.path,f=r.query,h=r.hash,l=r.params;if(f=a.hasOwnProperty("query")?a.query:f,h=a.hasOwnProperty("hash")?a.hash:h,l=a.hasOwnProperty("params")?a.params:l,c){i[c];return u({_normalized:!0,name:c,query:f,hash:h,params:l},void 0,r)}if(s){var d=lt(s,t),v=it(d,l,'redirect route with path "'+d+'"');return u({_normalized:!0,path:v,query:f,hash:h},void 0,r)}return p(null,r)}function s(t,e,r){var n=it(r,e.params,'aliased route with path "'+r+'"'),o=u({_normalized:!0,path:n});if(o){var i=o.matched,a=i[i.length-1];return e.params=o.params,p(a,e)}return p(null,e)}function p(t,r,n){return t&&t.redirect?c(t,n||r):t&&t.matchAs?s(t,r,t.matchAs):m(t,r,n,e)}return{match:u,addRoutes:a}}function ht(t,e,r){var n=e.match(t);if(!n)return!1;if(!r)return!0;for(var o=1,i=n.length;o<i;++o){var a=t.keys[o-1],u="string"===typeof n[o]?decodeURIComponent(n[o]):n[o];a&&(r[a.name||"pathMatch"]=u)}return!0}function lt(t,e){return q(t,e.parent?e.parent.path:"/",!0)}var dt=Object.create(null);function vt(){window.history.replaceState({key:At()},"",window.location.href.replace(window.location.origin,"")),window.addEventListener("popstate",function(t){mt(),t.state&&t.state.key&&Tt(t.state.key)})}function yt(t,e,r,n){if(t.app){var o=t.options.scrollBehavior;o&&t.app.$nextTick(function(){var i=gt(),a=o.call(t,e,r,n?i:null);a&&("function"===typeof a.then?a.then(function(t){_t(t,i)}).catch(function(t){0}):_t(a,i))})}}function mt(){var t=At();t&&(dt[t]={x:window.pageXOffset,y:window.pageYOffset})}function gt(){var t=At();if(t)return dt[t]}function wt(t,e){var r=document.documentElement,n=r.getBoundingClientRect(),o=t.getBoundingClientRect();return{x:o.left-n.left-e.x,y:o.top-n.top-e.y}}function bt(t){return Rt(t.x)||Rt(t.y)}function xt(t){return{x:Rt(t.x)?t.x:window.pageXOffset,y:Rt(t.y)?t.y:window.pageYOffset}}function kt(t){return{x:Rt(t.x)?t.x:0,y:Rt(t.y)?t.y:0}}function Rt(t){return"number"===typeof t}function _t(t,e){var r="object"===typeof t;if(r&&"string"===typeof t.selector){var n=document.querySelector(t.selector);if(n){var o=t.offset&&"object"===typeof t.offset?t.offset:{};o=kt(o),e=wt(n,o)}else bt(t)&&(e=xt(t))}else r&&bt(t)&&(e=xt(t));e&&window.scrollTo(e.x,e.y)}var Et=L&&function(){var t=window.navigator.userAgent;return(-1===t.indexOf("Android 2.")&&-1===t.indexOf("Android 4.0")||-1===t.indexOf("Mobile Safari")||-1!==t.indexOf("Chrome")||-1!==t.indexOf("Windows Phone"))&&(window.history&&"pushState"in window.history)}(),Ct=L&&window.performance&&window.performance.now?window.performance:Date,Ot=jt();function jt(){return Ct.now().toFixed(3)}function At(){return Ot}function Tt(t){Ot=t}function St(t,e){mt();var r=window.history;try{e?r.replaceState({key:Ot},"",t):(Ot=jt(),r.pushState({key:Ot},"",t))}catch(n){window.location[e?"replace":"assign"](t)}}function $t(t){St(t,!0)}function Lt(t,e,r){var n=function(o){o>=t.length?r():t[o]?e(t[o],function(){n(o+1)}):n(o+1)};n(0)}function qt(t){return function(e,r,n){var i=!1,a=0,u=null;Ut(t,function(t,e,r,c){if("function"===typeof t&&void 0===t.cid){i=!0,a++;var s,p=Mt(function(e){Vt(e)&&(e=e.default),t.resolved="function"===typeof e?e:C.extend(e),r.components[c]=e,a--,a<=0&&n()}),f=Mt(function(t){var e="Failed to resolve async component "+c+": "+t;u||(u=o(t)?t:new Error(e),n(u))});try{s=t(p,f)}catch(l){f(l)}if(s)if("function"===typeof s.then)s.then(p,f);else{var h=s.component;h&&"function"===typeof h.then&&h.then(p,f)}}}),i||n()}}function Ut(t,e){return Pt(t.map(function(t){return Object.keys(t.components).map(function(r){return e(t.components[r],t.instances[r],t,r)})}))}function Pt(t){return Array.prototype.concat.apply([],t)}var It="function"===typeof Symbol&&"symbol"===typeof Symbol.toStringTag;function Vt(t){return t.__esModule||It&&"Module"===t[Symbol.toStringTag]}function Mt(t){var e=!1;return function(){var r=[],n=arguments.length;while(n--)r[n]=arguments[n];if(!e)return e=!0,t.apply(this,r)}}var Bt=function(t,e){this.router=t,this.base=Ht(e),this.current=w,this.pending=null,this.ready=!1,this.readyCbs=[],this.readyErrorCbs=[],this.errorCbs=[]};function Ht(t){if(!t)if(L){var e=document.querySelector("base");t=e&&e.getAttribute("href")||"/",t=t.replace(/^https?:\/\/[^\/]+/,"")}else t="/";return"/"!==t.charAt(0)&&(t="/"+t),t.replace(/\/$/,"")}function zt(t,e){var r,n=Math.max(t.length,e.length);for(r=0;r<n;r++)if(t[r]!==e[r])break;return{updated:e.slice(0,r),activated:e.slice(r),deactivated:t.slice(r)}}function Ft(t,e,r,n){var o=Ut(t,function(t,n,o,i){var a=Dt(t,e);if(a)return Array.isArray(a)?a.map(function(t){return r(t,n,o,i)}):r(a,n,o,i)});return Pt(n?o.reverse():o)}function Dt(t,e){return"function"!==typeof t&&(t=C.extend(t)),t.options[e]}function Jt(t){return Ft(t,"beforeRouteLeave",Nt,!0)}function Kt(t){return Ft(t,"beforeRouteUpdate",Nt)}function Nt(t,e){if(e)return function(){return t.apply(e,arguments)}}function Xt(t,e,r){return Ft(t,"beforeRouteEnter",function(t,n,o,i){return Qt(t,o,i,e,r)})}function Qt(t,e,r,n,o){return function(i,a,u){return t(i,a,function(t){u(t),"function"===typeof t&&n.push(function(){Yt(t,e.instances,r,o)})})}}function Yt(t,e,r,n){e[r]&&!e[r]._isBeingDestroyed?t(e[r]):n()&&setTimeout(function(){Yt(t,e,r,n)},16)}Bt.prototype.listen=function(t){this.cb=t},Bt.prototype.onReady=function(t,e){this.ready?t():(this.readyCbs.push(t),e&&this.readyErrorCbs.push(e))},Bt.prototype.onError=function(t){this.errorCbs.push(t)},Bt.prototype.transitionTo=function(t,e,r){var n=this,o=this.router.match(t,this.current);this.confirmTransition(o,function(){n.updateRoute(o),e&&e(o),n.ensureURL(),n.ready||(n.ready=!0,n.readyCbs.forEach(function(t){t(o)}))},function(t){r&&r(t),t&&!n.ready&&(n.ready=!0,n.readyErrorCbs.forEach(function(e){e(t)}))})},Bt.prototype.confirmTransition=function(t,e,r){var i=this,a=this.current,u=function(t){o(t)&&(i.errorCbs.length?i.errorCbs.forEach(function(e){e(t)}):(n(!1,"uncaught error during route navigation:"),console.error(t))),r&&r(t)};if(k(t,a)&&t.matched.length===a.matched.length)return this.ensureURL(),u();var c=zt(this.current.matched,t.matched),s=c.updated,p=c.deactivated,f=c.activated,h=[].concat(Jt(p),this.router.beforeHooks,Kt(s),f.map(function(t){return t.beforeEnter}),qt(f));this.pending=t;var l=function(e,r){if(i.pending!==t)return u();try{e(t,a,function(t){!1===t||o(t)?(i.ensureURL(!0),u(t)):"string"===typeof t||"object"===typeof t&&("string"===typeof t.path||"string"===typeof t.name)?(u(),"object"===typeof t&&t.replace?i.replace(t):i.push(t)):r(t)})}catch(n){u(n)}};Lt(h,l,function(){var r=[],n=function(){return i.current===t},o=Xt(f,r,n),a=o.concat(i.router.resolveHooks);Lt(a,l,function(){if(i.pending!==t)return u();i.pending=null,e(t),i.router.app&&i.router.app.$nextTick(function(){r.forEach(function(t){t()})})})})},Bt.prototype.updateRoute=function(t){var e=this.current;this.current=t,this.cb&&this.cb(t),this.router.afterHooks.forEach(function(r){r&&r(t,e)})};var Wt=function(t){function e(e,r){var n=this;t.call(this,e,r);var o=e.options.scrollBehavior,i=Et&&o;i&&vt();var a=Gt(this.base);window.addEventListener("popstate",function(t){var r=n.current,o=Gt(n.base);n.current===w&&o===a||n.transitionTo(o,function(t){i&&yt(e,t,r,!0)})})}return t&&(e.__proto__=t),e.prototype=Object.create(t&&t.prototype),e.prototype.constructor=e,e.prototype.go=function(t){window.history.go(t)},e.prototype.push=function(t,e,r){var n=this,o=this,i=o.current;this.transitionTo(t,function(t){St(P(n.base+t.fullPath)),yt(n.router,t,i,!1),e&&e(t)},r)},e.prototype.replace=function(t,e,r){var n=this,o=this,i=o.current;this.transitionTo(t,function(t){$t(P(n.base+t.fullPath)),yt(n.router,t,i,!1),e&&e(t)},r)},e.prototype.ensureURL=function(t){if(Gt(this.base)!==this.current.fullPath){var e=P(this.base+this.current.fullPath);t?St(e):$t(e)}},e.prototype.getCurrentLocation=function(){return Gt(this.base)},e}(Bt);function Gt(t){var e=decodeURI(window.location.pathname);return t&&0===e.indexOf(t)&&(e=e.slice(t.length)),(e||"/")+window.location.search+window.location.hash}var Zt=function(t){function e(e,r,n){t.call(this,e,r),n&&te(this.base)||ee()}return t&&(e.__proto__=t),e.prototype=Object.create(t&&t.prototype),e.prototype.constructor=e,e.prototype.setupListeners=function(){var t=this,e=this.router,r=e.options.scrollBehavior,n=Et&&r;n&&vt(),window.addEventListener(Et?"popstate":"hashchange",function(){var e=t.current;ee()&&t.transitionTo(re(),function(r){n&&yt(t.router,r,e,!0),Et||ie(r.fullPath)})})},e.prototype.push=function(t,e,r){var n=this,o=this,i=o.current;this.transitionTo(t,function(t){oe(t.fullPath),yt(n.router,t,i,!1),e&&e(t)},r)},e.prototype.replace=function(t,e,r){var n=this,o=this,i=o.current;this.transitionTo(t,function(t){ie(t.fullPath),yt(n.router,t,i,!1),e&&e(t)},r)},e.prototype.go=function(t){window.history.go(t)},e.prototype.ensureURL=function(t){var e=this.current.fullPath;re()!==e&&(t?oe(e):ie(e))},e.prototype.getCurrentLocation=function(){return re()},e}(Bt);function te(t){var e=Gt(t);if(!/^\/#/.test(e))return window.location.replace(P(t+"/#"+e)),!0}function ee(){var t=re();return"/"===t.charAt(0)||(ie("/"+t),!1)}function re(){var t=window.location.href,e=t.indexOf("#");return-1===e?"":decodeURI(t.slice(e+1))}function ne(t){var e=window.location.href,r=e.indexOf("#"),n=r>=0?e.slice(0,r):e;return n+"#"+t}function oe(t){Et?St(ne(t)):window.location.hash=t}function ie(t){Et?$t(ne(t)):window.location.replace(ne(t))}var ae=function(t){function e(e,r){t.call(this,e,r),this.stack=[],this.index=-1}return t&&(e.__proto__=t),e.prototype=Object.create(t&&t.prototype),e.prototype.constructor=e,e.prototype.push=function(t,e,r){var n=this;this.transitionTo(t,function(t){n.stack=n.stack.slice(0,n.index+1).concat(t),n.index++,e&&e(t)},r)},e.prototype.replace=function(t,e,r){var n=this;this.transitionTo(t,function(t){n.stack=n.stack.slice(0,n.index).concat(t),e&&e(t)},r)},e.prototype.go=function(t){var e=this,r=this.index+t;if(!(r<0||r>=this.stack.length)){var n=this.stack[r];this.confirmTransition(n,function(){e.index=r,e.updateRoute(n)})}},e.prototype.getCurrentLocation=function(){var t=this.stack[this.stack.length-1];return t?t.fullPath:"/"},e.prototype.ensureURL=function(){},e}(Bt),ue=function(t){void 0===t&&(t={}),this.app=null,this.apps=[],this.options=t,this.beforeHooks=[],this.resolveHooks=[],this.afterHooks=[],this.matcher=ft(t.routes||[],this);var e=t.mode||"hash";switch(this.fallback="history"===e&&!Et&&!1!==t.fallback,this.fallback&&(e="hash"),L||(e="abstract"),this.mode=e,e){case"history":this.history=new Wt(this,t.base);break;case"hash":this.history=new Zt(this,t.base,this.fallback);break;case"abstract":this.history=new ae(this,t.base);break;default:0}},ce={currentRoute:{configurable:!0}};function se(t,e){return t.push(e),function(){var r=t.indexOf(e);r>-1&&t.splice(r,1)}}function pe(t,e,r){var n="hash"===r?"#"+e:e;return t?P(t+"/"+n):n}ue.prototype.match=function(t,e,r){return this.matcher.match(t,e,r)},ce.currentRoute.get=function(){return this.history&&this.history.current},ue.prototype.init=function(t){var e=this;if(this.apps.push(t),!this.app){this.app=t;var r=this.history;if(r instanceof Wt)r.transitionTo(r.getCurrentLocation());else if(r instanceof Zt){var n=function(){r.setupListeners()};r.transitionTo(r.getCurrentLocation(),n,n)}r.listen(function(t){e.apps.forEach(function(e){e._route=t})})}},ue.prototype.beforeEach=function(t){return se(this.beforeHooks,t)},ue.prototype.beforeResolve=function(t){return se(this.resolveHooks,t)},ue.prototype.afterEach=function(t){return se(this.afterHooks,t)},ue.prototype.onReady=function(t,e){this.history.onReady(t,e)},ue.prototype.onError=function(t){this.history.onError(t)},ue.prototype.push=function(t,e,r){this.history.push(t,e,r)},ue.prototype.replace=function(t,e,r){this.history.replace(t,e,r)},ue.prototype.go=function(t){this.history.go(t)},ue.prototype.back=function(){this.go(-1)},ue.prototype.forward=function(){this.go(1)},ue.prototype.getMatchedComponents=function(t){var e=t?t.matched?t:this.resolve(t).route:this.currentRoute;return e?[].concat.apply([],e.matched.map(function(t){return Object.keys(t.components).map(function(e){return t.components[e]})})):[]},ue.prototype.resolve=function(t,e,r){var n=pt(t,e||this.history.current,r,this),o=this.match(n,e),i=o.redirectedFrom||o.fullPath,a=this.history.base,u=pe(a,i,this.mode);return{location:n,route:o,href:u,normalizedTo:n,resolved:o}},ue.prototype.addRoutes=function(t){this.matcher.addRoutes(t),this.history.current!==w&&this.history.transitionTo(this.history.getCurrentLocation())},Object.defineProperties(ue.prototype,ce),ue.install=$,ue.version="3.0.2",L&&window.Vue&&window.Vue.use(ue),e["a"]=ue}}]);