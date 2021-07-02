using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Text;

namespace AirQualityDataProcessing.Model
{
    public class Instance
    {
        public String typeId { get; set; }
        public String name { get; set; }
        public List<String> timeSeriesId { get; set; }
        
    }
}
