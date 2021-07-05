using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Text;

namespace AirQualityDataProcessing.Model
{
    public class Type
    {
        internal bool contentType;


        public String id { get; set; }
        public TwinModel model { get; set; }

        public class TwinModel
        {
            public List<ModelContent> contents { get; set; }

            public class ModelContent
            {
                public String name { get; set; }
                public String schema { get; set; }
                [JsonProperty("@type")]
                public List<String> contentType { get; set; }
            }
        }
    }
}
