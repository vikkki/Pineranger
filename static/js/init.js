(function ($) {
  $(function () {


    // Plugin initialization
    $('.collapsible').collapsible({ accordion: true });
    $('.carousel.carousel-slider').carousel({ fullWidth: true });
    $('.carousel').carousel();
    $('.dropdown-trigger').dropdown({
      alignment: 'right',
      constrainWidth: false,
      coverTrigger: false,
      closeOnClick: false,
      onOpenEnd: function (el) {
        console.log(el.M_Dropdown);
        var tabs = $(this).find('.tabs');
        var dropdownInstance = el.M_Dropdown;
        if (tabs.length) {
          var tabsInstance = M.Tabs.getInstance(tabs);
          tabsInstance.updateTabIndicator();
          tabsInstance.options.onShow = function () {
            setTimeout(function () {
              dropdownInstance.recalculateDimensions();
              tabsInstance.updateTabIndicator();
            }, 0);
          };
        }
      }
    });
    $('.slider').slider();
    $('.parallax').parallax();
    $('.modal').modal();
    $('.scrollspy').scrollSpy();
    $('.sidenav').sidenav({ 'edge': 'left' });
    $('#sidenav-right').sidenav({ 'edge': 'right' });
    $('.datepicker').datepicker({ selectYears: 20 });
    $('select').not('.disabled').formSelect();
    $('input.autocomplete').autocomplete({
      data: { "Apple": null, "Microsoft": null, "Google": 'http://placehold.it/250x250' },
    });
    $('.tabs').tabs();




  }); // end of document ready
})(jQuery); // end of jQuery name space
