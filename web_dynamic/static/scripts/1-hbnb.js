$(document).ready(function () {
    let selectedAmenities = {};

    $('input[type="checkbox"]').change(function () {
        if (this.checked) {
            selectedAmenities[$(this).data('id')] = $(this).data('name');
        } else {
            delete selectedAmenities[$(this).data('id')];
        }

        let amenityNames = Object.values(selectedAmenities).join(', ');
        if (amenityNames.length === 0) {
            amenityNames = '&nbsp;';
        }
        $('.amenities h4').html(amenityNames);
    });
});

