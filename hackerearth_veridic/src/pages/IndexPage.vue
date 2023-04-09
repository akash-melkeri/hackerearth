<template>
  <q-page class="">
    <q-header bordered class="no-shadow">
      <q-toolbar>
        <!-- <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        /> -->
        <q-icon name="newspaper" size="md" />
        <q-toolbar-title>
          Veridic Solutions
        </q-toolbar-title>

        <!-- <a href="https://github.com/akash-melkeri">
          <q-btn round flat dense >
            <svg class="text-white" viewBox="0 0 32 32"><path fill="currentColor" fill-rule="evenodd" d="M16 2a14 14 0 0 0-4.43 27.28c.7.13 1-.3 1-.67v-2.38c-3.89.84-4.71-1.88-4.71-1.88a3.71 3.71 0 0 0-1.62-2.05c-1.27-.86.1-.85.1-.85a2.94 2.94 0 0 1 2.14 1.45a3 3 0 0 0 4.08 1.16a2.93 2.93 0 0 1 .88-1.87c-3.1-.36-6.37-1.56-6.37-6.92a5.4 5.4 0 0 1 1.44-3.76a5 5 0 0 1 .14-3.7s1.17-.38 3.85 1.43a13.3 13.3 0 0 1 7 0c2.67-1.81 3.84-1.43 3.84-1.43a5 5 0 0 1 .14 3.7a5.4 5.4 0 0 1 1.44 3.76c0 5.38-3.27 6.56-6.39 6.91a3.33 3.33 0 0 1 .95 2.59v3.84c0 .46.25.81 1 .67A14 14 0 0 0 16 2Z"/></svg>
          </q-btn>
        </a> -->
      </q-toolbar>
    </q-header>

    <!-- <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      behavior="mobile"
    >
      <q-list>
        <q-item-label
          header
        >
          Essential Links
        </q-item-label>

        
      </q-list>
    </q-drawer> -->
    <div>
      <div class="tw-pt-4 tw-px-4">
        <q-input dense outlined placeholder="Search" v-model="search">
          <template v-slot:append>
            <q-icon name="search" color="primary" />
          </template>
        </q-input>
      </div>
      <div v-if="not_found" class="tw-bg-gray-100 tw-m-4 tw-rounded-lg tw-h-96 flex flex-center column">
        <svg xmlns="http://www.w3.org/2000/svg" class="tw-text-teal-700 tw-h-16 tw-animate-bounce" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 7v4a1 1 0 0 0 1 1h3m0-5v10m3-9v8a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1V8a1 1 0 0 0-1-1h-2a1 1 0 0 0-1 1zm7-1v4a1 1 0 0 0 1 1h3m0-5v10"/></svg>
        <div class="tw-text-gray-500">The requested resource is not found.</div>
      </div>
      <div v-else>
        <div v-if="is_loaded && posts.length > 0" class="tw-grid tw-grid-cols-1 sm:tw-grid-cols-2 md:tw-grid-cols-3 lg:tw-grid-cols-4 tw-gap-4 tw-p-4 sm:tw-gap-6 md:tw-gap-8">
          <div v-for="post in filterBy(posts,search)" class="tw-border tw-rounded-lg tw-overflow-hidden hover:tw-shadow-xl hover:tw-scale-105 tw-ease-out tw-duration-200" :key="post.id" >
            <a :href="post.link" target="_blank">
              <div >
                <q-img class="tw-h-48 tw-aspect-video" :src="post.jetpack_featured_media_url"></q-img>
              </div>
              <div class="tw-p-4 ">
                <div v-html="post.title.rendered" class="tw-text-lg tw-font-bold ellipsis-2-lines tw-break-words tw-mb-2">
                </div>
                <div v-html="post.excerpt.rendered" class="tw-text-gray-600 tw-break-words ellipsis-3-lines tw-mb-4"></div>
                <div class="tw-text-gray-400 tw-pb-4">
                  <q-icon name="schedule" />
                  <span class="tw-text-xs tw-pl-2">{{ new Date(post.date).toLocaleTimeString() }} {{ new Date(post.date).toDateString() }}</span>
                </div>
                <a :href="post.link" class="tw-w-full" target="_blank">
                  <q-btn no-caps class="tw-w-full tw-bg-sky-900 tw-text-white" flat >
                    <q-icon name="open_in_new" />
                    <span class="tw-pl-2">Open</span>
                  </q-btn>
                </a>
              </div>
            </a>
          </div>
        </div>
        <div v-else-if="is_loaded && posts.length == 0" class="tw-bg-gray-100 tw-m-4 tw-rounded-lg tw-h-96 flex flex-center column">
          <svg xmlns="http://www.w3.org/2000/svg" class="tw-text-teal-700 tw-h-16 tw-animate-bounce" viewBox="0 0 256 256"><path fill="currentColor" d="M210.3 35.9L23.9 88.4a8 8 0 0 0-1.2 15l85.6 40.5a7.8 7.8 0 0 1 3.8 3.8l40.5 85.6a8 8 0 0 0 15-1.2l52.5-186.4a7.9 7.9 0 0 0-9.8-9.8Z" opacity=".2"/><path fill="currentColor" d="M223.7 32.3a15.9 15.9 0 0 0-15.6-4.1L21.8 80.7a16.1 16.1 0 0 0-2.6 29.9l85.7 40.5l40.5 85.7a16 16 0 0 0 14.4 9.1h1.4a15.9 15.9 0 0 0 14.1-11.6l52.5-186.4a15.9 15.9 0 0 0-4.1-15.6Zm-63.8 197.6l-39.4-83.1l41.3-41.3a8 8 0 1 0-11.3-11.3l-41.3 41.3l-83.1-39.4l186.3-52.5Z"/></svg>
          <div class="tw-text-gray-500 tw-mt-4">No posts for now.</div>
        </div>
        <div v-else-if="!is_loaded" class="tw-bg-gray-100 tw-m-4 tw-rounded-lg tw-h-96 flex flex-center column">
          <q-spinner size="32px" color="primary"></q-spinner>
          <div class="tw-text-gray-500 tw-mt-4">Looking for latest posts</div>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
import { defineComponent, ref } from 'vue'
import EssentialLink from 'components/EssentialLink.vue'

const linksList = [
  {
    title: 'Docs',
    caption: 'quasar.dev',
    icon: 'school',
    link: 'https://quasar.dev'
  },
  {
    title: 'Github',
    caption: 'github.com/quasarframework',
    icon: 'code',
    link: 'https://github.com/quasarframework'
  },
  {
    title: 'Discord Chat Channel',
    caption: 'chat.quasar.dev',
    icon: 'chat',
    link: 'https://chat.quasar.dev'
  },
  {
    title: 'Forum',
    caption: 'forum.quasar.dev',
    icon: 'record_voice_over',
    link: 'https://forum.quasar.dev'
  },
  {
    title: 'Twitter',
    caption: '@quasarframework',
    icon: 'rss_feed',
    link: 'https://twitter.quasar.dev'
  },
  {
    title: 'Facebook',
    caption: '@QuasarFramework',
    icon: 'public',
    link: 'https://facebook.quasar.dev'
  },
  {
    title: 'Quasar Awesome',
    caption: 'Community Quasar projects',
    icon: 'favorite',
    link: 'https://awesome.quasar.dev'
  }
]

export default defineComponent({
  name: 'IndexPage',
  components: {
    EssentialLink
  },
  setup () {
    const leftDrawerOpen = ref(false)

    return {
      essentialLinks: linksList,
      leftDrawerOpen,
      toggleLeftDrawer () {
        leftDrawerOpen.value = !leftDrawerOpen.value
      },
      posts:ref([]),
      search:ref(''),
      not_found:ref(false),
      is_loaded:ref(false),

    }
  },
  methods:{
    fetchPosts(){
      let self = this
      self.$axios.get('https://techcrunch.com/wp-json/wp/v2/posts?per_page=20&context=embed').then((response)=>{
        if(response.status == 200){
          self.posts = response.data
        }else if(response.status == 404){
          console.log('fetch Failed');
          self.not_found = true
        }
        console.log(response.data);
        self.is_loaded = true
      }).catch((error)=>{
        console.log(error);
        self.is_loaded = true
      })
    },
    filterBy (arr, search) {
      function contains (val, search) {
    var i
    if (util.isPlainObject(val)) {
        var keys = Object.keys(val)
        i = keys.length
        while (i--) {
        if (contains(val[keys[i]], search)) {
            return true
        }
        }
    } else if (util.isArray(val)) {
        i = val.length
        while (i--) {
        if (contains(val[i], search)) {
            return true
        }
        }
    } else if (val != null) {
        return val.toString().toLowerCase().indexOf(search) > -1
    }
  }
var util = {};

util.isString = function(item) {
    return typeof item==='string';
};

util.isUndefined = function(item) {
    return typeof item==='undefined';
};

util.isNull = function(item) {
  return typeof item == null;
};

util.isArray = function (obj) {
    return Array.isArray(obj);
};

util.isNumber = function(item) {
    return typeof item === "number";
};
util.convertToDecimal = function convertToDecimal(num, decimal){
  return Math.round(num * Math.pow(10,decimal)) / (Math.pow(10, decimal));
};

util.objectContains=function objectContains(partial, object) {
  let keys = Object.keys(partial);
  return keys.map(function(el) {
    return (object[el] !== undefined) && (object[el] == partial[el]);
  }).indexOf(false) == -1;

};

util.hasApproxPattern=function hasApproxPattern(word, pattern) {
  // cheaper version of indexOf; instead of creating each
  // iteration new str.
  function indexOf(word, p, c) {
    var j = 0;
    while ((p + j) <= word.length) {
      if (word.charAt(p + j) == c) return j;
      j++;
    }
    return -1;
  }
  var p = 0;
  for (var i = 0; i <= pattern.length; i++) {
    var index = indexOf(word, p, pattern.charAt(i));
    if (index == -1) return false;
    p += index + 1;
  }
  return true
}

util.toArray=function toArray(object) {
  return util.isArray(object)
    ? object
    : Object.keys(object).map(function(key) {
      return object[key];
    });
};
util.convertRangeToArray = function (range) {
  return [...Array(range + 1).keys()].slice(1)
};

util.isObject = function(obj) {
    var type = typeof obj;
    return type === 'function' || type === 'object' && !!obj;
};
util.isFunction = function(obj) {
    return typeof obj === 'function'
};

util.toArray = function(list, start) {
  start = start || 0
  var i = list.length - start
  var ret = new Array(i)
  while (i--) {
    ret[i] = list[i + start]
  }
  return ret
};

util.toNumber = function(value) {
  if (typeof value !== 'string') {
    return value
  } else {
    var parsed = Number(value)
    return isNaN(parsed)
      ? value
      : parsed
  }
};


util.convertArray = function (value) {
    if (util.isArray(value)) {
      return value
    } else if (util.isPlainObject(value)) {
      // convert plain object to array.
      var keys = Object.keys(value)
      var i = keys.length
      var res = new Array(i)
      var key
      while (i--) {
        key = keys[i]
        res[i] = {
          $key: key,
          $value: value[key]
        }
      }
      return res
    } else {
      return value || []
    }
}

function multiIndex(obj,is) {  // obj,['1','2','3'] -> ((obj['1'])['2'])['3']
    return is.length ? multiIndex(obj[is[0]],is.slice(1)) : obj
}

util.getPath = function(obj,is) {   // obj,'1.2.3' -> multiIndex(obj,['1','2','3'])
    return multiIndex(obj,is.split('.'))
}

/**
 * Strict object type check. Only returns true
 * for plain JavaScript objects.
 *
 * @param {*} obj
 * @return {Boolean}
 */

var toString = Object.prototype.toString
var OBJECT_STRING = '[object Object]'
util.isPlainObject = function (obj) {
  return toString.call(obj) === OBJECT_STRING
}

util.exist = function(value) {
  return value !== null && typeof value !== 'undefined'
}

      var arr = util.convertArray(arr)
      if (search == null) {
        return arr
      }
      if (typeof search === 'function') {
        return arr.filter(search)
      }
      // cast to lowercase string
      search = ('' + search).toLowerCase()
      var n = 2
      // extract and flatten keys
      var keys = Array.prototype.concat.apply([], util.toArray(arguments, n))
      var res = []
      var item, key, val, j
      for (var i = 0, l = arr.length; i < l; i++) {
        item = arr[i]
        val = (item && item.$value) || item
        j = keys.length
        if (j) {
          while (j--) {
            key = keys[j]
            if ((key === '$key' && contains(item.$key, search)) ||
                contains(util.getPath(val, key), search)) {
              res.push(item)
              break
            }
          }
        } else if (contains(item, search)) {
          res.push(item)
        }
      }
      return res
    },
  },
  created(){
    // console.log('hello',this.$axios);
    this.fetchPosts()
    // console.log();
  }
})
</script>
