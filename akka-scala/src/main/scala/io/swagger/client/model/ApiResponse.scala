/**
 * iRepoter
 * iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that need government intervention around the community  Checkout the API on [Github](https://github.com/JamesMudidi/iReporterApi/tree/develop-v2) 
 *
 * OpenAPI spec version: 2.0
 * Contact: mudidi.jimmy@gmail.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */
package io.swagger.client.model

import io.swagger.client.core.ApiModel
import org.joda.time.DateTime
import java.util.UUID

case class ApiResponse (
  code: Option[Int] = None,
  `type`: Option[String] = None,
  message: Option[String] = None
) extends ApiModel


