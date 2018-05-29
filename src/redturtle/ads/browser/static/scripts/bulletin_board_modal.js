requirejs(["jquery", "mockup-patterns-modal"], function($, Modal){

  function render_modal(el){
    modal = new Modal($(el), {
      content: '#content',
      actionOptions:{
        timeout: 20000,
        redirectOnResponse: true,
      }
    });
  }
  $(document).ready(function(){
    $('a.load-modal').each(function(i, el) {
      render_modal(el)
    });
  });
});
